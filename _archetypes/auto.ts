import {slugify} from "https://deno.land/x/slugify/mod.ts";

enum Card {
	Story,
	Boon,
	Waylay
}

interface Output {
	path: string,
	content: Record<string, string>
}

export default async function* auto(fn:string):Output {
	var out;
	const in=Deno.readTextFile(fn)
	switch(fn.split('.')[1]) /*filext*/ {
		case 'json': out=JSON.parse(await in); break;
		case 'yml':
		case 'yaml':
			import { parse } from "jsr:@std/yaml";
			out=parse(await in)
			break;
		case 'toml':
			import { parse } from "jsr:@std/toml";
			out=parse(await in)
			break;
		default: throw new TypeError('can only support files in the format json, yaml, or toml.')
	}
	for(const i of out) yield i;
}
			
