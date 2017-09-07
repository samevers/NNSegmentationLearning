#!/usr/bin/python


import sys

import numpy as np

SEED = 123
#np.random.seed(SEED)

corpus = []
inputfile= sys.argv[1]
  
FIN = open(inputfile, 'r')
for line in FIN.readlines():
	line = line.strip()
	corpus.append(line)
FIN.close()

shuffleScale = 0
if len(sys.argv) > 2:
  shuffleScale= int(sys.argv[2])
else:
  shuffleScale= len(corpus)

idx= np.arange(len(corpus))
np.random.shuffle(idx)
idx = idx[:shuffleScale]
data = (corpus[n] for n in idx)

for q in data:
	sys.stdout.write("%s\n" % q)
