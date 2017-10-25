
# wc -l all.tsv = 117565
triples :
	python3 process_kb.py3 < movieqa/knowledge_source/wiki_entities/wiki_entities_kb.txt |shuf > all.tsv
	head -80000 all.tsv > train.tsv
	head -90000 all.tsv |tail -10000 > test.tsv
	tail -10000 all.tsv > val.tsv
	rm all.tsv 

movies.vocab :
	python3 process_kb.py3 < movieqa/knowledge_source/wiki_entities/wiki_entities_kb.txt \
  | cut -f1,2 | tr '\t' '\n' | sort -u |grep -v '^[0-9]*$$' |grep -v '^.$$' > $@
	
relations.txt :
	python3 process_kb.py3 < movieqa/knowledge_source/wiki_entities/wiki_entities_kb.txt |cut -f3 |sort -u > $@

