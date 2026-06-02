for i in boon waylay story; do
deno run --allow-read=. --allow-write=. collate.ts $i
done
