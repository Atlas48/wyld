if $(return >/dev/null 2>&1); then #script is sourced
	function mkcard {
		deno run --allow-write=card --allow-import mkcard.ts $@
	}
else
	deno run --allow-write=card --allow-import mkcard.ts $@
fi
