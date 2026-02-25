import { extname } from "@std/path/extname";
import { exists } from "jsr:@std/fs/exists";
import { encodeBase64 } from "@std/encoding/base64";

function qlookup(s:string):string {
	const sd=s.slice(1)
	switch(sd) {
		case 'jpg': return 'image/jpeg';
		case 'svg': return 'image/svg+xml';
		default: return 'image/'+sd;
	}
}

const td = new TextDecoder;

export default async function datauri(fn:string): Promise<string> {
	if(!(await exists('card/img/'+fn))) return '';
	const fd=Deno.readFile('card/img/'+fn);
	const en=extname(fn);
	if(en==='.svg') return `data:image/svg+xml,${encodeURIComponent(td.decode(await data))}`
	else return `data:${qlookup(en)};base64,${encodeBase64(await fd)}`
}
