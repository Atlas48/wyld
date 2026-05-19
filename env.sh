export WYLDROOT=`pwd`
alias lume="deno run lume"
function deactivate {
	unalias lume
	unset WYLDROOT
	unset -f deactivate
}
