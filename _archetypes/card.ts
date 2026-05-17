import {slugify} from "https://deno.land/x/slugify/mod.ts";
import {slugconf} from "../lib.ts";

export default function card(type:string,title:string,content:string) {
	const base=`/card/${type}/${slugify(title,slugconf)}.`;
	return {
		path: base+'md',
		content: {
			title,
			layout: "card.pug",
			url: base+'svg',
			special: false,
			content
		}
	}
}
