import lume from "lume/mod.ts";
import pug from "lume/plugins/pug.ts";

const conf = {
	prettyUrls: false
};

const site = lume(conf);

site.use(pug());
site.add("card/img");

export default site;
