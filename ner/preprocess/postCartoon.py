#!/usr/bin/python
#coding:gbk
import sys,os,re

regex = re.compile(r'\!|\?|\.|\-|\_|\+|\=|\"|\<|\>|\,|\~|？|！|。|，| |	')
for line in sys.stdin:
	line = line.strip()
	line,n = re.subn(regex, "", line)	
	print line
