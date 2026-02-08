export default function(data: Lume.Data) {
  const pages = data.search.pages(`type=${data.type} test!=true`).filter((p: Lume.Data) => !p.url.match(/\/test-[^/]+$/));
  const cards = pages.map((page: Lume.Data, i: number) => ({
    name: page.title,
    type: "base",
    description: page.content || "",
    system: {},
    suit: data.type,
    value: page.xp ?? null,
    back: {
		name: "Wyld Card",
		text: "",
		img: ""
	},
    faces: [{ name: page.title, img: `/${data.type}/${page.url.replace(/.*\//, '').replace(/\.[^.]+$/, '')}.svg`, text: "" }],
    face: null,
    drawn: false,
    origin: null,
    width: null,
    height: null,
    rotation: 0,
    sort: i * 100000,
    flags: {},
  }));

  const deck = {
    name: data.title,
    type: "deck",
    description: data.description || "",
    img: "",
    system: {},
    cards,
    width: null,
    height: null,
    rotation: 0,
    displayCount: false,
    ownership: { default: 0 },
    flags: {},
    folder: null,
    sort: 0,
  };

  return JSON.stringify(deck);
};
