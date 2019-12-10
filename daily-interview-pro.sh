#!/bin/bash

function daily-interview-pro {
	mkdir "$1";
	cd "$1";
	touch solution.py README.md;
	echo "# "$2"" > README.md;
}

question=$2
fileseq=$1
filename=`echo $2 | sed 's/ /\_/g'`
dirname=${fileseq}_${filename}
echo "Created folder ${dirname}"
daily-interview-pro $dirname $question


