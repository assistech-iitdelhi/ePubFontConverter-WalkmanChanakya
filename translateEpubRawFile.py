# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from bs4 import Tag, NavigableString
# import cssutils
import convert as asciitohin
import sys
import re
import copy

def match_class(target):                                                        
    def do_match(tag):                                                          
        classes = tag.get('class', [])         
        return all(c in classes for c in target)                                
    return do_match

def replaceText(soup, font):
	if(soup.string is None):
		for x in soup:
			replaceText(x, font)
	else:
		soup.string.replace_with(asciitohin.convertToUni(soup.string.encode('utf-8'), font))

inp = open(sys.argv[1], 'r')
feed = inp.read()
inp.close()
soup = BeautifulSoup(feed, 'html.parser')
#Changing it for removing span from here
with open('soupbeforeconvertandspanremoval.txt', 'a') as html:
    html.write(str(soup))
#invalid_tags=['<span xml:lang="en-US">','</span>','<span>']
soupstr=str(soup)
count=1
while (count!=0):
	result=re.subn(r'(?P<cop>(<span)(.*?)(>))(.*?)(<\/span>)( *)(?P=cop)',r'\1\5\7',soupstr)
	soupstr=result[0]
	count=result[1]	
#	count=result[1]
with open('soupbeforeconvert.txt', 'a') as html:
    html.write(soupstr)
soup = BeautifulSoup(soupstr, "html.parser")
#Done till here
allt = soup.body.find_all(recursive = False)
alltags = [BeautifulSoup(unicode(str(soup.body.find_all(match_class(['englishMeaning']))[i]),"utf-8")).body.contents[0] for i in range(0,len(soup.body.find_all(match_class(['englishMeaning']))))]
#printing allt and alltag
#allt_print=open("alltafterspanremoval.txt","a")
#allt_print.write(str(allt))
#allt_print.close()
#alltags_print=open("alltags.txt","a")
#alltags_print.write(str(alltags))
#alltags_print.close()
#Done printing till here
for t in allt:
	replaceText(t,int(sys.argv[2]))
alltagsn = soup.body.find_all(match_class(['englishMeaning']))

for i in range(0,len(alltags)):
	alltagsn[i].replace_with(alltags[i])

print soup
