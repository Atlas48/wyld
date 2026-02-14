import lume from "lume/mod.ts";
import pug from "lume/plugins/pug.ts";

const conf = {
	prettyUrls: false
};

const site = lume(conf);
var cards=new Map;

function preprocess_md(pages) {
	for (const page of pages) {
		if (page.data.url?.endsWith('.svg')) {
			cards.set(page.data.type, cards.get(page.data.type) || []);
			cards.get(page.data.type).push({
				title: page.data.title,
				url: page.data.url,
				xp: page.data.xp,
				content: page.data.content,
				perpetual: page.data.perpetual,
				img: page.data.img,
			});
		}
	}
}

site.preprocess([".md"], preprocess_md);
site.data('cards',cards);
site.use(pug());
site.add("card/img");

export default site;
