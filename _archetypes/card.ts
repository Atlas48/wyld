import {slugify} from "https://deno.land/x/slugify/mod.ts";
import argparse from "https://github.com/denoboot/argparse/raw/refs/heads/main/src/mod.ts";

const apconf: argparse.Options = {
	alias: {
		i: "image",
		x: "xp",
		s: "special"
	},
	default: {
		xp: 0,
		special: false
	}
}

export default function card() {
	const args=argparse(arguments,apconf);
	const base=`/card/${args._[0]}/${slugify(args._[1],{lower:true})}.`;
	var out = {
		path: base+'md',
		content: {
			title: args._[1],
			layout: "card.pug",
			url: base+'svg',
			special: args.special,
			content: args._[2]??""
		}
	}
	if(args._[0]=="story") out.content.xp=args.xp;
	return out;
}
