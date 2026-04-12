import textLoader from "lume/core/loaders/text.ts";

export class TXTEngine implements Lume.Engine {
	render(s:string) { return s; }
	addHelper() {}
	deleteCache() {}
}
export default function html() {
	return function(site:Lume.Site) {
		const opt = {
			loader: textLoader,
			engine: new TXTEngine
		}
		site.loadPages(['.txt'],opt);
	}
}
