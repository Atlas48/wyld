import lume from "lume/mod.ts";
import pug from "lume/plugins/pug.ts";
import {conf,mdconf} from './lib.ts';

const site = lume(conf,mdconf);

site.use(pug());
site.add("card/img");

export default site;
