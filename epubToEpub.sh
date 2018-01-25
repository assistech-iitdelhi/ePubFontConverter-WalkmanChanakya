#!/bin/bash
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
# non-unicode to unicode conversion 
# of NCERT ePathShala epub file to unicode epub file
# capturing the entire formatting

# Usage : ./runepub.sh <filename_without_extension> <option>
# filename_without_extension : fname if document us fname.epub
# option : 1 :- for walkman chanakya
#		   2 :- for user uploaded mapping

if [ -d $1 ] 
then
	rm -rf $1
fi

unzip $1.epub -d $1
if [ $? -ne 0 ] 
then
	echo "---------- Corrupted file: "$1".epub -----------"
	rm $1.epub
	exit 0
fi

# sudo chmod -R 777 $1
chap=$(find -name "*.html" -or -name "*.xhtml")
for ch in $chap
do
	echo '==================='
	echo $ch
	touch temp.txt
	python translateEpubRawFile.py $ch $2 > temp.txt
	cp temp.txt $ch
	rm temp.txt
done

mkdir epubout
cd $1
zip -r $1n.epub *
cp $1n.epub ../epubout/$1.epub
cd ..
# chmod 777 $1out.epub
rm -rf $1

IFS=$SAVEIFS