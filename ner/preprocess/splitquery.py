#!/usr/bin/python
#coding:gbk
import sys,os,re

for line in sys.stdin:
	line = line.strip()
	try:
		tmp = line.decode("gbk")
		for t in tmp:
			sys.stdout.write("%s " % t.encode("gbk"))
	except:
		continue
	sys.stdout.write("\n")

