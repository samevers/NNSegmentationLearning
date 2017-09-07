#!/usr/bin/python
#coding:gbk
import sys,os,re

punc_ = {}
fin = open("punctuation.dic", 'r')
for line in fin.readlines():
	line = line.strip()
	punc_[line] = 1
fin.close()

####
alphaBetRex = re.compile(r'[a-zA-Z]+')
numRex = re.compile(r'[0-9]+')
for line in sys.stdin:
	line = line.strip()
	# 对query中的第一个实体进行标注
	line = "<s>" + " <s> " + line + " </s> " + " </s>"
	arr = line.split(" ")
	feats = ""
	begin = -1
	end = -1
	for i in range(2, len(arr) - 3):
		word = arr[i]
		if word == "#_#":
			continue
		feats = word
	
		flag_1 = 0
		word_1 = arr[i - 1]
		if arr[i - 1] == "#_#":
			word_1 = arr[i - 2]
			flag_1 = 1
		t1 = word_1 + arr[i]
		feats += " [T1]" + t1

		word_2 = arr[i - 2]
		if arr[i - 2] == "#_#" or flag_1 == 1:
			word_2 = arr[i - 3]
		t2 = word_2 + word_1 + word
		feats += " [T2]" + t2

		c_2 = word_2
		feats += " [S]C-2=" + c_2

		c_1 = word_1
		feats += " [S]C-1=" + c_1

		c_0 = word
		feats += " [S]C0=" + c_0

		word1 = arr[i + 1]
		flag1 = 0
		if arr[i + 1] == "#_#":
			word1 = arr[i + 2]
			flag1 = 1
		c1 = word1
		feats += " [S]C1=" + c1

		word2 = arr[i + 2]
		if arr[i + 2] == "#_#" or flag1 == 1:
			word2 = arr[i + 3]
		c2 = word2
		feats += " [S]C2=" + c2

		c_2_1 = word_2 + word_1
		feats += " [S]C-2C-1=" + c_2_1

		c_1_0 = word_1 + word
		feats += " [S]C-1C0=" + c_1_0

		c_0_1 = word + word1
		feats += " [S]C0C1=" + c_0_1

		c_1_2 = word1 + word2
		feats += " [S]C1C2=" + c_1_2

		c_1c1 = word_1 + word1
		feats += " [S]C-1C1=" + c_1c1

		c_0_2 = word + word2
		feats += " [S]C0C2=" + c_0_2

		v = "0"
		if word == word_2:
			v = "1"
		feats += " [S]RC0C-2=" + v

		v = "0"
		if word == word_1:
			v = "1"
		feats += " [S]RC0C-1=" + v

		c_1c0c1 = word_1 + word + word1
		feats += " [S]C-1C0C1=" + c_1c0c1

		## type
		v0 = ""
		malpha = alphaBetRex.match(arr[i])
		mnum = numRex.match(arr[i])
		if arr[i] in punc_:
			v = "0"
		elif malpha:
			v = "1"
		elif mnum:
			v = "3"
		else:
			v = "4"	
		feats += " [S]TC-1=" + v

		v_1 = ""
		malpha = alphaBetRex.match(word_1)
		mnum = numRex.match(word_1)
		if word_1 in punc_:
			v_1 += "0"
		elif malpha:
			v_1 += "1"
		elif mnum:
			v_1 += "3"
		else:
			v_1 += "4"	

		v1 = ""
		malpha = alphaBetRex.match(word1)
		mnum = numRex.match(word1)
		if word1 in punc_:
			v1 += "0"
		elif malpha:
			v1 += "1"
		elif mnum:
			v1 += "3"
		else:
			v1 += "4"	

		feats += " [S]TC-11=" + v_1 + v + v1

		v_2 = ""
		malpha = alphaBetRex.match(word_2)
		mnum = numRex.match(word_2)
		if word_2 in punc_:
			v_2 += "0"
		elif malpha:
			v_2 += "1"
		elif mnum:
			v_2 += "3"
		else:
			v_2 += "4"	

		v2 = ""
		malpha = alphaBetRex.match(word2)
		mnum = numRex.match(word2)
		if word2 in punc_:
			v2 += "0"
		elif malpha:
			v2 += "1"
		elif mnum:
			v2 += "3"
		else:
			v2 += "4"	

		feats += " [S]TC-22=" + v_2 + v_1 + v + v1 + v2
		## make tag
		if arr[i - 1] == "#_#" and end == -1:
			feats += " b-seg"
			begin = 1
		elif arr[i + 1] == "#_#":
			feats += " e-seg"
			end = 1
		elif begin == 1 and end == -1:
			feats += " i-seg"
		else:
			feats += " s-seg"

		print feats
	print ""
	#[T1]
	#[T2]
	#[S]C-2
	#[S]C-1
	#[S]C0
	#[S]C1
	#[S]C2
	#[S]C-2C-1
	#[S]C-1C0
	#[S]C0C1
	#[S]C1C2
	#[S]C-1C1
	#[S]C0C2
	#[S]RC0C-2
	#[S]RC0C-1
	#[S]C-1C0C1
	#[S]TC-1
	#[S]TC-11
	#[S]TC-22
	#tag
