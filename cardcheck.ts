import { bold } from "@std/fmt/colors";
var cards:Set<string>=new Set;
var images:Set<string>=new Set;
var stat:Promise<string[]>[]=new Array;

const perm=Deno.permissions.querySync({name:"read",path:'.'});
if(perm.state!=="granted") {
	console.error("please run with --allow-read=.")
	Deno.exit(1)
}

async function getcontents(dir:"img"|"boon"|"waylay"|"story"): Promise<string[]> {
	var out:string[]=new Array;
	for await(const i of Deno.readDir('card/'+dir)) {
		if(!i.isFile) continue;
		if(!i.name.match(/\.txt/)||i.name.match(/test/)) continue;
		out.push(i.name.replace(/\.txt/i,''));
	}
	return out;
}

async function* ygetcontents(dir:"img"|"boon"|"waylay"|"story"): AsyncGenerator<string> {
	for await(const i of Deno.readDir('card/'+dir)) {
		if(!i.isFile) continue;
		if(!i.name.match(/\.(?:sv|pn|jpe?)g/i)||i.name.match(/test/)) continue;
		yield i.name.replace(/\.(?:sv|pn|jpe?)g/i,'');
	}
}

stat.push(getcontents("boon"))
stat.push(getcontents("waylay"))
stat.push(getcontents("story"))
try {
	const res=await Promise.all(stat);
	for await(const ii of res)
		for(const i of ii) cards.add(i);
	for await(const i of ygetcontents("img")) images.add(i);
} catch(e) {
	console.error(`Program encountered an error: ${e}`)
}

if(!cards.size) console.error("cards set is empty.");
if(!images.size) console.error("images set is empty.");

console.log(bold("Outstanding files:"));
for(const i of cards.difference(images)) console.log(i);
