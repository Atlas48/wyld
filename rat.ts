const w = Number(Deno.args[0]);
const h = Number(Deno.args[1]);

if (!w || !h) {
  console.error("Requires a height and a width argument.");
  Deno.exit(1);
}

let new_w: number, new_h: number;

if (w * 5 <= h * 7) {
  new_w = w;
  new_h = Math.round(w * 5 / 7);
} else {
  new_w = Math.round(h * 7 / 5);
  new_h = h;
}

console.log(`${new_w}x${new_h}`);
