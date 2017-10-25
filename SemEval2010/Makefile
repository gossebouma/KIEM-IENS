rawtriples.tsv :
	egrep '(e1|Other)' SemEval2010_task8_training/TRAIN_FILE.TXT \
     |  sed -e 's///' -e 's/.*<e1>//' -e 's/<\/e1>.*<e2>/\t/' -e 's/<\/e2>.*//' \
     |  tr '\n' '\t' \
     |  sed -e 's/Other\t/Other\n/g' -e 's/)\t/)\n/g' \
     |  grep -v Comment \
     |  grep -v ' ' \
     |  tr 'A-Z' 'a-z' \
     |  sort -u > $@

e1e2: rawtriples.tsv
	grep 'e1,e2' $< |sed 's/(e1,e2)//' > $@
e2e1: rawtriples.tsv
	grep 'e2,e1' $< |sed 's/(e2,e1)//' |sed 's/\(.*\)\t\(.*\)\t/\2\t\1\t/' > $@

triples.tsv : e1e2 e2e1
	cat e1e2 e2e1 > $@
	grep -w other rawtriples.tsv >> $@

# 7010 lines 
shuf.tsv : triples.tsv
	shuf $< > $@

train.tsv : shuf.tsv
	head -5610 $< > $@
test.tsv : shuf.tsv
	tail -1400 $< | head -700 > $@
val.tsv : shuf.tsv
	tail -700 $< > $@

#corpus
semeval.txt :
	grep '^[0-9]' SemEval2010_task8_training/TRAIN_FILE.TXT |cut -f2 |sed -e 's/<e[12]>//g' -e 's/<\/e[12]>//g' -e 's/^"//' -e 's/"\s$$//' > $@
