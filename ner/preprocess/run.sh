#! /bin/bash
############################################
#
# Author: 
# E-Mail:huyonghua@sogou-inc.com
# Create time: 2017 9ÔÂ 07 16Ê±15·Ö02Ãë
# version 1.0
#
############################################
#cat sogou_query.20170217.1.query | python makeTag.py > sogou_query.20170217.1.query.cartoonTag
#cat sogou_query.20170217.1.query.cartoonTag | grep "#_#" > sogou_query.20170217.1.query.cartoonTag.cartoon
#cat sogou_query.20170217.1.query.cartoonTag | grep -v "#_#" > sogou_query.20170217.1.query.cartoonTag.noCartoon
#cat sogou_query.20170217.1.query.cartoonTag.cartoon | perl postCartoon.pl > x
#mv x sogou_query.20170217.1.query.cartoonTag.cartoon
#cat sogou_query.20170217.1.query.cartoonTag.cartoon | python splitCartoon.py > sogou_query.20170217.1.query.cartoonTag.cartoon.split
#cat sogou_query.20170217.1.query.cartoonTag.noCartoon | python splitquery.py > sogou_query.20170217.1.query.cartoonTag.noCartoon.split

## Split data
echo "5000 line of [*cartoon.split] to [test.split]"
head -5000 sogou_query.20170217.1.query.cartoonTag.cartoon.split > test.split
echo "5000 line of [*cartoon.split] to [dev.split]"
head -10000 sogou_query.20170217.1.query.cartoonTag.cartoon.split | tail -5000 > dev.split
lineNum=`wc -l sogou_query.20170217.1.query.cartoonTag.cartoon.split |awk -F" " '{print $1}'`
tailNum=$[$lineNum - 10000]
echo "$tailNum line of [*cartoon.split] to [train.split]"
tail -$tailNum sogou_query.20170217.1.query.cartoonTag.cartoon.split > train.split

scaleCommon=$[$lineNum * 5]
echo $scaleCommon
python shuffle.py sogou_query.20170217.1.query.cartoonTag.noCartoon.split $scaleCommon > x
mv x sogou_query.20170217.1.query.cartoonTag.noCartoon.split

echo "5000 line of [*noCartoon.split] added to [test.split]"
head -5000  sogou_query.20170217.1.query.cartoonTag.noCartoon >> test.split
echo "5000 line of [*noCartoon.split] added to [dev.split]"
head -10000 sogou_query.20170217.1.query.cartoonTag.noCartoon.split | tail -5000 >> dev.split
lineNum=`wc -l sogou_query.20170217.1.query.cartoonTag.noCartoon.split |awk -F" " '{print $1}'`
tailNum=$[$lineNum - 10000]
echo "$tailNum line of [*noCartoon.split] added to [train.split]"
tail -$tailNum sogou_query.20170217.1.query.cartoonTag.noCartoon.split >> train.split


## shuffle
echo "shuffle [*.split] files"
python shuffle.py train.split > train.shuffle.split
python shuffle.py test.split > test.shuffle.split
python shuffle.py dev.split > dev.shuffle.split

## make Feats
echo "Generate [*.feats] files"
cat train.shuffle.split | python makeFeats.py > train.shuffle.split.feats
cat test.shuffle.split | python makeFeats.py > test.shuffle.split.feats
cat dev.shuffle.split | python makeFeats.py > dev.shuffle.split.feats

## Iconv feats files
echo "Iconv [*.feats] from gbk to utf8"
iconv -c -f gbk -t utf8 train.shuffle.split.feats > ../pku/pku.sample.train.feats
iconv -c -f gbk -t utf8 dev.shuffle.split.feats > ../pku/pku.sample.dev.feats
iconv -c -f gbk -t utf8 test.shuffle.split.feats > ../pku/pku.test.feats

## embedding
echo "Run word2vec processing"
cat train.shuffle.split.feats test.shuffle.split.feats dev.shuffle.split.feats > train.feats
cd word2vec
ln -s ../train.feats .
#sh demo-word.sh

## Generate char.vec, bichar.vec, trichar.vec
echo "Generate [*char.vec.gbk] files"
cat train.feats.bin | awk '$0 !~/^\[/' > char.vec.gbk
cat train.feats.bin | awk '$0 ~/^\[T1\]/' > bichar.vec.gbk
cat train.feats.bin | awk '$0 ~/^\[T2\]/' > trichar.vec.gbk

## Iconv to utf8
echo "Generate [*char.vec] files, by <Iconv> ops"
iconv -c -f gbk -t utf8 char.vec.gbk > ../../embeddings/char.vec
iconv -c -f gbk -t utf8 bichar.vec.gbk > ../../embeddings/bichar.vec
iconv -c -f gbk -t utf8 trichar.vec.gbk > ../../embeddings/trichar.vec


## Back to the workspace directory
cd ../../
