
# assume that ../../../UKWAC/UKWAC-11_plain.tzt.gz has been unzipped

dbpediaUKWACWannacry_resource : dbpediaUKWACWannacry.triples dbpediaUKWACWannacryPaths.txt dbpediaUKWACWannaCryEntities.txt 
	mkdir -p dbpediaUKWACWannacry_paths_and_entities
	python ../create_resource_from_corpus.py dbpedia.triples dbpediaUKWACWannacry_paths_and_entities/dbpediaUKWACWannacry

UKWAC-11_plain.paths :
	python ../parse_wikipedia_open_vocab.py ../../../UKWAC/$*.txt $@

dbpediaUKWACWannacry.triples: UKWAC-11_plain.paths
	cat $< ../Wikipedia/A[ABCD]/*.dbpedia.paths  ../../../Wannacry/security.triples \
     |  sed -r 's/_[0-9]+_[0-9]+//g' > $@

dbpediaUKWACWannacryPaths.txt : dbpediaUKWACWannacry.triples
	cut -f3 $< | sort | uniq -c | grep -vw [1234] | cut -b9- > $@
	mkdir -p dbpediaUKWACWannacry_paths_and_entities
	ln -s $@ dbpediaUKWACWannacry_paths_and_entities/.

UKWACEntities.txt : UKWAC-11_plain.paths
	cut -f1,2 $< |tr '\t' '\n' |sort -u > $@

dbpediaUKWACWannaCryEntities.txt : UKWACEntities.txt
	cat ../Wikipedia/dbpedia.vocab UKWACEntities.txt ../../../Wannacry/security_entities.txt |sort -u > $@
	mkdir -p dbpediaUKWACWannacry_paths_and_entities
	ln -s $@ dbpediaUKWACWannacry_paths_and_entities/.



