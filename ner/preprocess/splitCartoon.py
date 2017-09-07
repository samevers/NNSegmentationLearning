#!/usr/bin/python
#coding:gbk
import sys,os,re

for line in sys.stdin:
	line = line.strip()
	arr = line.split("#_#")
	for term in arr:
		tmp = ""
		try:
			tmp = term.decode("gbk")
			for t in tmp:
				sys.stdout.write("%s " % t.encode("gbk"))
		except:
			sys.stdout.write("%s " % term)
		sys.stdout.write(" #_# ")
	sys.stdout.write("\n")

