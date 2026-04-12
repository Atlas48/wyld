import {slugify} from "https://deno.land/x/slugify/mod.ts";

const slugopt = {
	lower: true,
	remove: /[!"£$%^*()\[\];'#:@~`'<>?,.\/|\\]/g
}

export default function card(type:string,title:string,content:string) {
	const base=`/card/${type}/${slugify(title,slugopt)}.`;
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
