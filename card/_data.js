export default function url(p) {
	if(p.type =='story' || p.type=='boon' || p.type=='waylay') return `/${p.type}/${p.id}.svg`;
	else return `${p.id}.html`;
}
