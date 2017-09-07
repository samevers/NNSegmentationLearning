#!/usr/bin/python

import sys,os,re

def sub_(query):                                   
     arr = {}                                      
     try:                                          
         q_tmp = query.decode("gb18030")           
     except:                                       
         return arr                                
     size = len(q_tmp)                             
     for i in range(0,size):                       
         sub = ""                                  
         for j in range(i,size):                   
             sub = sub + q_tmp[j].encode("gb18030")
             arr[sub] = 1                          
     return arr

#######
hashname = {}
#fin = open("people.name", 'r')
fin = open("cartoon.dic", 'r')
for line in fin.readlines():
	line = line.strip()
	hashname[line] = 1
fin.close()

for line in sys.stdin:
	line = line.strip()
	arr = sub_(line)
	for term in arr:
		if term in hashname:
			toRep = "#_#" + term + "#_#"
			line,num = re.subn(term,toRep, line)
	print line
