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
	while(f.readSync(buf)==null) {
		const c=d.decode(buf);
		case(c) {
			case "\r":
				yield out;
				out='';
				break;
			default:
				out+=c;
				break;
		}
	}
	if(line) yield line;
}

export default function* md2story(inf:string) {
	for(const i of _slurp(inf)) {
		if(i[0]!='#'&&i[1]!=' ') continue;
		const title=i.substring(2);
		const base=`/card/story/${slugify(title,slugopt)}.`;
		yield {
			path: base+'md',
			content: {
				title,
				layout: 'card.pug',
				url: base+'svg',
				special: false
				content: ''
			}
		}
	}
}
