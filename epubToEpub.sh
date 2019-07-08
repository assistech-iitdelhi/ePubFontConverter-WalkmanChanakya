#!/bin/bash
#
# Extract epub file and call translateEpubRawFile on contained html/xhtml
#

justname=$(basename "$1" .epub)
justpath=$(dirname "$1")

unzip $1 -d "/tmp/$justname"
chapters=$(find /tmp/$justname -name '*.html' -o -name '*.xhtml')
for chapter in $chapters
do
	echo "CONVERTING $chapter of $1"
	python translateEpubRawFile.py $chapter > "/tmp/$justname.html"
	cp "/tmp/$justname.html" $chapter
done

zip -r "$justpath/$justname-converted.epub" "/tmp/$justname"
