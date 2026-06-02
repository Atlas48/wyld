switch(Deno.args[0]) {
	case 'boon':
	case 'waylay':
	case 'story': break;
	default:
		console.error("first argument must be either 'boon', 'waylay', or 'story', please.'");
		console.log(Deno.args)
		Deno.exit(1)
}
const root=Deno.env.get('WYLDROOT')+'/card/';
//means we don't do anything we don't need to!
import { extractYaml as extractYAML } from "@std/front-matter";

function trans(o) {
	var out=structuredClone(o.attrs);
	out.content=o.body.trimEnd();
	return out;
}
async function deref(a) {
	var out=[];
	for await(const i of a) out.push(trans(extractYAML(await i)));
	return out;
}
let all=[];
for await(const i of Deno.readDir(root+Deno.args[0])) {
	if (i.isDirectory||i.isSymlink) {
		console.error("caught non-file: "+i.name)
		continue;
	} //shouldn't happen
	if(i.name.startsWith('test')) continue;
	if(!i.name.endsWith('.txt')) continue;
	try {
		all.push(Deno.readTextFile(`card/${Deno.args[0]}/${i.name}`));
	} catch(e) {
		console.error(`Encountered error with ${i.name}, ${e}`)
		continue;
	}
}
await Promise.all(all);
let out=await deref(all);
Deno.writeTextFileSync(Deno.args[0]+'.json',JSON.stringify(out));
