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

def isit(string):
	temp="englishMeaning"
	index=0
	if(len(string)>15):
		while(index!=(len(string)-1)):
			t=string[index:(index+14)]
			if(t==temp):
				return False
			else:
				index=index+1
	return True

def sty(string):
	index=0
	count=1
	spacecount=0
	while(count!=0):
		count=0
		index=0
		#print '1'
		while(index!=len(string)):
			temp=string[index:(index+5)]
			#print temp
			if temp == "<span":
		#		print '2'
				index=index+4
				stor=index
				while(string[index]!='>'):
					index=index+1
				cop=string[(stor+1):(index+1)]
		#		print '3'
				while(string[index:(index+6)]!="</span" and index!=len(string)-1):
					index=index+1
				stor2=index
		#		print '4'
				while(string[index]!='>' and index!=len(string)-1):
					index=index+1
				stor3=index
				index=index+1
		#		print '5'
				substr=''
				while(string[index:(index+5)]!="<span" and index!=len(string)-1):
					if(string[index]!='<'):
						substr=substr+string[index]
						index=index+1
						spacecount=spacecount+1
					else:
						index=stor3+1
						break
				stor4=index
		#		print '6'
				index=index+4
				index=index+1
				if (cop==string[index:(index+len(cop))] and isit(cop)==True):
					stor5=index+len(cop)-1
					string1=string[:(stor2)]
					string2=string[stor5+1:]
					string=string1
					if(spacecount!=0):
						string=string+substr
						spacecount=spacecount-1
					string=string+string2
		#			print string2
					count=count+1
					index=index-4-(stor4-stor2)
				else:
					index=index-5
			else:
				index=index+1
	return string


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
#with open('soupbeforeconvertandspanremoval.txt', 'a') as html:
#    html.write(str(soup))
#invalid_tags=['<span xml:lang="en-US">','</span>','<span>']
soupstr=str(soup)
soupstr = re.sub(r"<!--(.|\s|\n)*?-->", "", soupstr)
#count=1
#while (count!=0):
#	result=re.subn(r'(?P<cop>(<span)(.*?)(>))(.*?)(<\/span>)( *)(?P=cop)',r'\1\5\7',soupstr)
#	soupstr=result[0]
#	count=result[1]	
#	count=result[1]
soupstr=sty(soupstr)
#with open('soupbeforeconvert.txt', 'a') as html:
#    html.write(soupstr)
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
