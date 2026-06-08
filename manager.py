#!/usr/bin/env python3
"""Wyldcard card management GUI. Requires: pyyaml"""

import re
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from pathlib import Path
import yaml
from PIL import Image, ImageTk
from lib.const import CARD_DIR, COLLECTIONS



def slugify(title: str) -> str:
	return re.sub(r"\s+", "-", re.sub(r'[!"£$%^*()\[\];\'#:@~`<>?,./|\\]', "", title.lower()).strip())


def list_cards(collection: str) -> list[str]:
	return sorted(p.stem for p in (CARD_DIR / collection).glob("*.md") if not p.stem.startswith("test"))

def read_card(collection: str, slug: str) -> dict:
	text = (CARD_DIR / collection / f"{slug}.txt").read_text(encoding="utf-8")
	parts = text.split("---\n", 2)
	if len(parts) < 3:
		return {"title": slug, "content": text}
	front = yaml.safe_load(parts[1]) or {}
	front["content"] = parts[2].strip()
	return front

def write_card(collection: str, slug: str, data: dict):
	front = {
		"title":   data.get("title", ""),
		"layout":  "card.pug",
		"url":     f"/card/{collection}/{slug}.svg",
		"special": bool(data.get("special", False)),
	}
	for key in ("desc", "img"):
		if data.get(key):
			front[key] = data[key]
	try:
		xp = int(data.get("xp") or 0)
		if xp:
			front["xp"] = xp
	except (ValueError, TypeError):
		pass
	(CARD_DIR / collection / f"{slug}.txt").write_text(
		f"---\n{yaml.dump(front, default_flow_style=False, allow_unicode=True)}---\n{data.get('content', '').strip()}\n",
		encoding="utf-8",
	)

def delete_card(collection: str, slug: str):
	(CARD_DIR / collection / f"{slug}.txt").unlink()


class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Wyldcard Manager")
		self._slugs: dict[str, list[str]] = {c: [] for c in COLLECTIONS}
		self._current: tuple[str | None, str | None] = (None, None)
		self._build()
		self._refresh_list()

	def _build(self):
		self.columnconfigure(1, weight=1)
		self.rowconfigure(0, weight=1)

		left = ttk.Frame(self, width=240)
		left.grid(row=0, column=0, sticky="ns", padx=(6, 0), pady=6)
		left.grid_propagate(False)
		left.rowconfigure(0, weight=1)
		left.columnconfigure(0, weight=1)
		left.columnconfigure(1, weight=1)

		self.nb = ttk.Notebook(left)
		self.nb.grid(row=0, column=0, sticky="nsew", columnspan=2)
		self.nb.bind("<<NotebookTabChanged>>", lambda _: self._refresh_list())

		self.listboxes: dict[str, tk.Listbox] = {}
		for col in COLLECTIONS:
			f = ttk.Frame(self.nb)
			self.nb.add(f, text=col.capitalize())
			f.rowconfigure(0, weight=1)
			f.columnconfigure(0, weight=1)
			sb = ttk.Scrollbar(f, orient=tk.VERTICAL)
			lb = tk.Listbox(f, yscrollcommand=sb.set, activestyle="none",
				selectmode=tk.SINGLE, exportselection=False)
			sb.config(command=lb.yview)
			lb.grid(row=0, column=0, sticky="nsew")
			sb.grid(row=0, column=1, sticky="ns")
			lb.bind("<<ListboxSelect>>", self._on_select)
			self.listboxes[col] = lb

		ttk.Button(left, text="New",    command=self._new_card   ).grid(row=1, column=0, sticky="ew", pady=(4, 0))
		ttk.Button(left, text="Delete", command=self._delete_card).grid(row=1, column=1, sticky="ew", pady=(4, 0))

		right = ttk.Frame(self)
		right.grid(row=0, column=1, sticky="nsew", padx=6, pady=6)
		right.columnconfigure(1, weight=1)
		right.rowconfigure(5, weight=1)

		self.f_title = ttk.Entry(right)
		self.f_desc  = ttk.Entry(right)
		self.f_xp    = ttk.Spinbox(right, from_=0, to=10, width=5)

		for i, (lbl, w) in enumerate(zip(
			("Title", "Desc", "XP"),
			(self.f_title, self.f_desc, self.f_xp)
		)):
			ttk.Label(right, text=lbl).grid(row=i, column=0, sticky="w", padx=(0, 6))
			w.grid(row=i, column=1, sticky="ew", pady=2)
		ttk.Label(right, text="Img").grid(row=3, column=0, sticky="w", padx=(0, 6))

		img_row = ttk.Frame(right)
		img_row.grid(row=3, column=1, sticky="ew", pady=2)
		img_row.columnconfigure(0, weight=1)
		self.f_img = ttk.Entry(img_row)
		self.f_img.grid(row=0, column=0, sticky="ew")
		self.btn_preview = ttk.Button(img_row, text="Preview", command=self._preview_image)
		v_img = tk.StringVar()
		v_img.trace_add("write", lambda *_: (
			self.btn_preview.grid(row=0, column=1, padx=(4, 0)) if v_img.get().strip()
			else self.btn_preview.grid_remove()
		))
		self.f_img.config(textvariable=v_img)
		self.btn_preview.grid_remove()

		self.v_special = tk.BooleanVar()
		ttk.Checkbutton(right, text="Special", variable=self.v_special).grid(row=4, column=1, sticky="w")

		ttk.Label(right, text="Body").grid(row=5, column=0, sticky="nw", pady=(4, 0))
		self.f_body = tk.Text(right, wrap=tk.WORD, undo=True)
		sb_body = ttk.Scrollbar(right, orient=tk.VERTICAL, command=self.f_body.yview)
		self.f_body.config(yscrollcommand=sb_body.set)
		self.f_body.grid(row=5, column=1, sticky="nsew", pady=(4, 0))
		sb_body.grid(row=5, column=2, sticky="ns", pady=(4, 0))

		ttk.Button(right, text="Save", command=self._save_card).grid(
			row=6, column=0, columnspan=3, sticky="ew", pady=(6, 0))

	def _current_collection(self) -> str:
		return COLLECTIONS[self.nb.index(self.nb.select())]

	def _refresh_list(self, select_slug: str | None = None):
		col = self._current_collection()
		self._slugs[col] = list_cards(col)
		lb = self.listboxes[col]
		lb.delete(0, tk.END)
		for i, s in enumerate(self._slugs[col]):
			lb.insert(tk.END, s)
			if s == select_slug:
				lb.selection_set(i)
				lb.see(i)

	def _on_select(self, _event=None):
		col = self._current_collection()
		sel = self.listboxes[col].curselection()
		if not sel:
			return
		slug = self._slugs[col][sel[0]]
		self._current = (col, slug)
		data = read_card(col, slug)
		self.f_title.delete(0, tk.END);  self.f_title.insert(0, data.get("title", ""))
		self.f_desc.delete(0, tk.END);   self.f_desc.insert(0, data.get("desc", "") or "")
		self.f_xp.delete(0, tk.END);     self.f_xp.insert(0, str(data.get("xp") or 0))
		self.f_img.delete(0, tk.END);    self.f_img.insert(0, data.get("img", "") or "")
		self.v_special.set(bool(data.get("special", False)))
		self.f_body.delete("1.0", tk.END)
		self.f_body.insert("1.0", data.get("content", ""))
		self.f_body.edit_reset()

	def _preview_image(self):
		col, slug = self._current
		if col is None:
			return
		data = read_card(col, slug)
		img_path = CARD_DIR / "img" / (data.get("img") or f"{slug}.png")
		if img_path.suffix.lower() not in (".png", ".jpg", ".jpeg") or not img_path.exists():
			messagebox.showinfo("No image", f"No image found for {slug}.")
			return
		win = tk.Toplevel(self)
		win.title(img_path.name)
		img = Image.open(img_path)
		photo = ImageTk.PhotoImage(img)
		lbl = tk.Label(win, image=photo)
		lbl.image = photo
		lbl.pack()

	def _save_card(self):
		col, slug = self._current
		if col is None:
			messagebox.showwarning("Nothing selected", "Select or create a card first.")
			return
		title = self.f_title.get().strip()
		if not title:
			messagebox.showwarning("Missing title", "Title is required.")
			return
		write_card(col, slug, {
			"title":   title,
			"desc":    self.f_desc.get().strip(),
			"xp":      self.f_xp.get(),
			"img":     self.f_img.get().strip(),
			"special": self.v_special.get(),
			"content": self.f_body.get("1.0", tk.END).strip(),
		})
		self._refresh_list(select_slug=slug)

	def _new_card(self):
		col = self._current_collection()
		title = simpledialog.askstring("New card", "Title:", parent=self)
		if not title:
			return
		slug = slugify(title)
		write_card(col, slug, {"title": title, "special": False, "content": ""})
		self._refresh_list(select_slug=slug)
		self._on_select()

	def _delete_card(self):
		col, slug = self._current
		if col is None:
			return
		if messagebox.askyesno("Delete", f"Delete '{slug}'?"):
			delete_card(col, slug)
			self._current = (None, None)
			self._refresh_list()


if __name__ == "__main__":
	App().mainloop()
