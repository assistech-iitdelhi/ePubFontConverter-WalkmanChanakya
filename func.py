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
				if (cop==string[index:(index+len(cop))]):
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


inp=raw_input("Enter the text ")
print sty(inp)
