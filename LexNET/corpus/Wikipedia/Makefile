
# set up initial file structure and links
init :
	cp Makefile.sub AA/.
	cp Makefile.sub AB/.
	cp Makefile.sub AC/.
	cp Makefile.sub AD/.
	ln -s ../../../DBpedia/dbpedia.vocab .
	ln -s ../../../Babi/movies.vocab .
	mkdir dbpedia_paths_and_enttities
	ln -s dbpedia.vocab dbpedia_paths_and_entities/dbpediaEntities.txt
	mkdir movies_paths_and_enttities
	ln -s movies.vocab movies_paths_and_entities/moviesEntities.txt

# creating a corpus resource
dbpedia.triples:
	cat A[ABCD]/*.dbpedia.paths > $@

dbpediaPaths.txt : dbpedia.triples
	cut -f3 $< | sort | uniq -c | grep -vw [1234] | cut -b9- > $@
	ln -s $@ dbpedia_paths_and_entities/.

dbpedia_resource : dbpedia.triples dbpediaPaths.txt
	python ../create_resource_from_corpus.py dbpedia.triples dbpedia_paths_and_entities/dbpedia

# creating movies corpus resource
movies.triples:
	cat A[ABCD]/*.movies.paths > movies.triples

moviesPaths.txt :
	cut -f3 movies.triples | sort | uniq -c | grep -vw [1234] | cut -b9- > $@
	ln -s moviesPaths.txt movies_paths_and_entities/.

movies_resource : movies.triples moviesPaths.txt
	python ../create_resource_from_corpus.py movies.triples movies_paths_and_entities/movies
