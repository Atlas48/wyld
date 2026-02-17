for i in boon story waylay; do
	m4 -Dtype=$i templ.m4.ts > $i.ts
done
