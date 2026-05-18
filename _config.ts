import lume from "lume/mod.ts";
import pug from "lume/plugins/pug.ts";
import txt from './txt.ts';
import datauri from './datauri.ts'
import {conf,mdconf} from './lib.ts';

async function adduri(p) {
	for(const i of p) i.data.imguri = await datauri(i.data.img ? i.data.img : i.data.basename+'.png')
}

const site = lume(conf,mdconf);

site.use(pug());
site.use(txt());
site.preprocess(['.txt'],adduri);
site.ignore(i=>i.match(/.*plot.*\.md/i));
site.ignore("tk");
site.add("card/img");

export default site;
