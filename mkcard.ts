import {stringify} from "@std/yaml";
import {slugify} from "https://deno.land/x/slugify/mod.ts";
import argparse from "https://github.com/denoboot/argparse/raw/refs/heads/main/src/mod.ts";

const slugconf= {
	lower: true
}

const apconf:argparse.Options= {
	alias: {
		i: "image",
		x: "xp",
		p: "perpetual"
	},
	default: {
		image: "",
		xp: 0,
		perpetual: false
	}
}

const args=argparse(Deno.args,apconf);

if (args._.length!==2) {
	console.error("requires a type and a title.")
	Deno.exit(1)
}
var content="";
const d=new TextDecoder;
const stat=await Deno.permissions.query({name:"write",path:"./card"});
if (stat.state!=="granted") {
	console.error("Unable to write to cards directory, permission not granted")
	Deno.exit(1)
}
const outf:any={
	title:args._[1],
	img: args.image
}
switch(Deno.args[0]) {
	case "story": outf.xp=args.xp; break;
	case "boon": outf.perpetual=args.perpetual; break;
	case "waylay": break;
	default:
		console.error("First argument must be either story, boon, or waylay.");
		Deno.exit(1);
}
content+="---\n";
content+=stringify(outf);
content+="---\n";
if(!Deno.stdin.isTerminal()) for await (const i of Deno.stdin.readable) content+=d.decode(i);
await Deno.writeTextFile(`./card/${Deno.args[0]}/${slugify(Deno.args[1],slugconf)}.md`,content);
