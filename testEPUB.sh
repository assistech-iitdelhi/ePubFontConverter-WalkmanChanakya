#!/bin/bash
# sudo chmod -R 777 $1
chap=$(find t/input -name "*.html" -or -name "*.xhtml")
for ch in $chap
do
	echo '==================='
	python translateEpubRawFile.py $ch 1 > t/output/`basename $ch`
done
