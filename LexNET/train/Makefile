DIMENSIONS = 50
GLOVE = ../../glove/glove.6B.$(DIMENSIONS)d.txt
LAYERS = 0
# or 1

# standard data
BLESS :
	python train_integrated.py ../corpus/wiki/wiki ../datasets/BLESS BLESS_$(LAYERS)_$(DIMENSIONS) $(GLOVE) $(LAYERS)
EVAL :
	python train_integrated.py ../corpus/wiki/wiki ../datasets/EVALution EVAL_$(LAYERS)_$(DIMENSIONS) $(GLOVE) $(LAYERS)
KHN :
	python train_integrated.py ../corpus/wiki/wiki ../datasets/KHN KHN_$(LAYERS)_$(DIMENSIONS) $(GLOVE) $(LAYERS)
ROOT09 :
	python train_integrated.py ../corpus/wiki/wiki ../datasets/ROOT09 ROOT09_$(LAYERS)_$(DIMENSIONS) $(GLOVE) $(LAYERS)
# additional experiments
SEMEVAL:
	python train_integrated.py ../corpus/wiki/wiki ../datasets/SemEval2010 SEMEVAL_$(LAYERS)_$(DIMENSIONS) $(GLOVE) $(LAYERS)
DBPEDIA :
	python train_integrated.py ../corpus/wiki/wiki ../datasets/DBpedia DBPEDIA_$(LAYERS)_$(DIMENSIONS) $(GLOVE) $(LAYERS)
MOVIES:
	python train_integrated.py ../corpus/movies_paths_and_entities/movies ../datasets/BabiMovie MOVIES_$(LAYERS)_$(DIMENSIONS) $(GLOVE) $(LAYERS)
ITTOO :
	python train_integrated.py ../corpus/wiki/wiki ../datasets/Ittoo ITTOO_$(LAYERS)_$(DIMENSIONS) $(GLOVE) $(LAYERS)
	
# cross domain
UKWAC:
	python train_integrated.py ../corpus/WikipediaUKWACWannaCry/dbpediaUKWACWannaCry ../datasets/UKWAC UKWAC_$(LAYERS)_$(DIMENSIONS) $(GLOVE) $(LAYERS)
WANNACRY:
	python train_integrated.py ../corpus/WikipediaUKWACWannaCry/dbpediaUKWACWannaCry ../datasets/Wannacry Wannacry_$(LAYERS)_$(DIMENSIONS) $(GLOVE) $(LAYERS)
# testing dbpedia on merged corpus resource -- for checking only
DUW:
	python train_integrated.py ../corpus/WikipediaUKWACWannaCry/dbpediaUKWACWannaCry ../datasets/DBpedia DUW_$(LAYERS)_$(DIMENSIONS) $(GLOVE) $(LAYERS)

