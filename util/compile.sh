#!/bin/bash
for d in card/*; do
	for i in $d/*; do
		if [[ $i != *.toml ]]
			 then continue
		fi
		echo $i
		echo "[[card]]" >> all.toml
		echo "type=\"$(basename $d)\"" >> all.toml
		cat $i >> all.toml
	done
done
