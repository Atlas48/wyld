import {slugify} from "https://deno.land/x/slugify/mod.ts";

export default function card(type:string, title:string, text:string, special:string) {
	const base=`/card/${type}/${slugify(title,{lower:true})}.`;
	var out = {
		path: base+'md',
		content: {
			layout: "card.pug",
			url: base+'svg',
			content: text
		}
	}
	switch(type) {
		case "boon": out.content.perpetual=(typeof special !== "undefined" && special!==null) && (special[0]==="t" || special[0]==="y"); break;
		case "waylay": break; //nothing special to add!
		case "story": out.content.xp=parseInt(special); break;
		default:
			console.error("Please provide either 'boon', 'waylay', or 'story' as options")
			return undefined;
	} return out;
}
