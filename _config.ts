import lume from "lume/mod.ts";
import pug from "lume/plugins/pug.ts";
import deflist from "npm:markdown-it-deflist";

const conf = {
	prettyUrls: false
};

const mdconf = {
	plugins: [deflist]
}

const site = lume(conf);

site.use(pug());
site.add("card/img");

export default site;
