import {slugify} from "https://deno.land/x/slugify/mod.ts";

const slugopt = {
	lower: true,
	remove: /[!"£$%^*()\[\];'#:@~`'<>?,.\/|\\]/g
}

function* _slurp(inf:string): Iterable<string> {
	const d=new TextDecoder;
	const buf=new Uint8Array(1);
	const f=Deno.openSync(inf);
	var out='';
	while(f.readSync(buf)!=null) {
		const c=d.decode(buf);
		switch(c) {
			case "\r": continue;
			case "\n":
				yield out;
				out='';
				break;
			default:
				out+=c;
				break;
		}
	}
	if(out) yield out;
}

export default function* md2story(inf:string) {
	for(const i of _slurp(inf)) {
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
