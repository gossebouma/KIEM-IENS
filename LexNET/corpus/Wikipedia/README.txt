
do 

make init

to set up file structure.

Then copy or link Wikipedia txt in subdirectories AA AB AC AD (this should be the result from processing a raw wikipedia dump as indicated in the main Wikipedia directory)

Then run 

make -f Makefile.sub

in all subdirectories

and do 

make wikipedia_resource 

to create the corpus resource for Wikipedia/dbpedia 

All this takes quite some time and memory and disk space...


