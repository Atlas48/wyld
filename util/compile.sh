#!/bin/bash
for d in card/*; do
	for i in $d/*; do
		if [[ $i != *.toml ]]
			 then continue
		fi
		if [ "$1" == "-v" ]
			then echo $i
		fi
		echo "[[card]]" >> all.toml
		echo "type=\"$(basename $d)\"" >> all.toml
		cat $i >> all.toml
	done
done
