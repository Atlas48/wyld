if test -z $WYLDROOT; then
	echo "Please source env.sh before running"
	exit 1
fi
find $WYLDROOT/card/img -type f -exec identify -format "%f %w %h\n" {} + | awk '$2!=168||$3!=120{print}'
