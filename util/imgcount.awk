#!/usr/bin/awk -f
# imgcount.awk
# feed the input from imgchk.py into this!
# run with `p=1` to print alongside
BEGIN {
	total=undefined=null=missing=exists=0
}
$1=="X" {undefined++}
$1=="O" {null++}
$1=="~" {missing++}
$1=="-" {exists++}
p{print}
{total++}
END {
	if (p) print "===";
	incomplete=undefined+null+missing;
	print "total", total;
	print "exists", exists, (exists/total)*100 "%";
	print "incomplete", incomplete, (incomplete/total)*100 "%";
	print "undefined", undefined, (undefined/total)*100 "%";
	print "null", null, (null/total)*100 "%";
	print "missing", missing, (missing/total)*100 "%";
}
