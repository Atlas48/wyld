export default function(data: Lume.Data) {
  const pages = data.search.pages(`type=${data.type}`).filter((p: Lume.Data) => !!p.url && !p.url.match(/test-/));
  const cards = pages.map((page: Lume.Data, i: number) => ({
    name: page.title,
    type: "base",
    description: page.content || "",
    system: {},
    suit: data.type,
    value: page.xp??0,
    back: {
		name: `Wyld Card: ${type}`,
		text: "",
		img: ""
	},
    faces: [{ name: page.title, img: `/${data.type}/${page.url.replace(/.*\//, '').replace(/\.[^.]+$/, '')}.svg`, text: "" }],
    face: null,
    drawn: false,
    origin: null,
    width: data.conf.width,
    height: data.conf.height,
    rotation: 0,
    sort: i * 100000,
    flags: {},
  }));
  const deck = {
    name: "Wyld Cards: "+data.title,
    type: "deck",
    description: data.description || "",
    img: "",
    system: {},
    cards,
    width: data.conf.width,
    height: data.conf.height,
    rotation: 0,
    displayCount: false,
    ownership: { default: 0 },
    flags: {},
    folder: null,
    sort: 0,
  };
  return JSON.stringify(deck);
};
