
mero.tsv : all_uniq.seeds
	sed -e 's/$$/	mero/' -e 's/ /	/' $< > $@

random.tsv : mero.tsv
	cut -f1 $< |shuf > small.lst
	cut -f2 $< |shuf > big.lst
	paste small.lst big.lst | sed -e 's/$$/	random/' > $@
	rm small.lst big.lst

mero_random.tsv :
	cat shuffle.tsv random.tsv |shuf > $@

train.tsv : mero_random.tsv
	head -n 2454 $< > $@
test.tsv : mero_random.tsv
	tail -n 700 $< | head -n 350 > $@
val.tsv : mero_random.tsv
	tail -n 350 $< > $@
