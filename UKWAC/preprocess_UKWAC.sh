#!/bin/bash

for i in {1..25};
do
	gunzip -kc /net/corpora/UKWAC/"UKWAC-"$i".xml.gz" | cut -f1 | grep -v '</s>|<text.*>|</text>' -E | tr '\n' ' ' | sed 's/<s>/\n/g' | sed 's/^ //g' | grep '^$' -v | sed 's/ ([,.!?'\''])/\1/g' -E | iconv -f iso-8859-1 -t utf-8 > /net/corpora/UKWAC_plain/"UKWAC-"$i"_plain.txt"
done
