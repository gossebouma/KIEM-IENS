
# create triples from raw data
triples.txt :
	bzless mappingbased_objects_en.ttl.bz2 |grep 'dbpedia.org/ontology' \
  | sed -e 's/<http:\/\/dbpedia.org\/resource\/\([^>]*\)> <http:\/\/dbpedia.org\/ontology\/\([^>]*\)> <http:\/\/dbpedia.org\/resource\/\([^>]*\)> ./\1\t\3\t\2/' \
        -e 's/_/ /g' \
  | tr 'A-Z' 'a-z' \
  | grep -v '<http:\/\/' \
  > $@

# 100 most frequent relations (and filter 1 empty line)
relations.freq : 
	cut -f3 ../triples.txt | sort |uniq -c |sort -nr > $@

relations.txt : relations.freq
	head -100 $< |cut -c9- |grep '.' > $@

relations.pat : relations.txt 
	sed -e 's/^/\\b/' -e 's/$$/$$/' $< > $@

# only triples with top 100 relation, in random order
tsv : relations.pat
	grep -f $< ../triples.txt | shuf > shuf.txt
	head -1500000 shuf.txt > train.tsv
	head -1550000 shuf.txt | tail -50000 > test.tsv
	head -1600000 shuf.txt | tail -50000 > val.tsv
	rm shuf.txt

dbpedia.vocab :
	cut -f1,2 *.tsv |tr '\t' '\n' |sort -u > $@

