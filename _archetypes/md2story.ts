import {slugify} from "https://deno.land/x/slugify/mod.ts";
import {TextLineStream} from "jsr:@std/streams/text-line-stream";

async function* _slurp(inf: string): AsyncGenerator<string> {
    const file = await Deno.open(inf);
    const lines = file.readable
        .pipeThrough(new TextDecoderStream())
        .pipeThrough(new TextLineStream());
    for await (const line of lines) yield line;
}

export default async function* md2story(inf:string) {
	for await(const i of _slurp(inf)) {
		if(!i.match(/^# /)) continue;
		const title=i.substring(2);
		if(title.length>255) throw new TypeError(`Passed value that cannot be written: ${title}`);
		const base=`/card/story/${slugify(title,slugopt)}.`;
		if(Deno.existsSync(base+'txt')) continue;
		yield {
			path: base+'txt',
			content: {
				title,
				layout: 'card.pug',
				url: base+'svg',
				special: false,
				xp: 0,
				content: ''
			}
		}
	}
}
