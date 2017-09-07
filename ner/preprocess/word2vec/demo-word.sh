#! /bin/bash
#time ./bin/word2vec -train accuquery.filter.seg.post -output vectors.bin -cbow 0 -size 200 -window 5 -negative 0 -hs 1 -sample 1e-3 -threads 12 -binary 1
#time ./bin/word2vec -train sogou_query.txt.seg.test -output vectors.bin -cbow 0 -size 200 -window 5 -negative 0 -hs 1 -sample 1e-3 -threads 12 -binary 1
time ./bin/word2vec -train train.feats -output train.feats.bin -cbow 0 -size 50 -window 5 -negative 0 -hs 1 -sample 1e-3 -threads 12 -binary 0
#./bin/w2v-distance vectors.bin
