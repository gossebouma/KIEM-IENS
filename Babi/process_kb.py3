import re, sys

#pat = re.compile('[0-9]* (.*) ([a-z]*_[a-z_]*) (.*)')
pat = re.compile('[0-9]* (.*) ([a-z]*_[a-z_]*) (.*)')

for line in sys.stdin :
	m = pat.search(line)
	if m: 
		relation = m.group(2)
		if relation in ['directed_by','starred_actors','written_by','has_genre','has_tags','in_language'] :
			answers = re.split(', ',m.group(3))
			for answer in answers :
				print('{}\t{}\t{}'.format(m.group(1).lower(),answer.lower(),relation ) )
		else :
			True
	else :
		True

#  grep -o '[a-z]*_[a-z_]*' movieqa/knowledge_source/wiki_entities/wiki_entities_kb.txt |sortnr
#  17341 has_plot
#  16726 release_year
#  15234 directed_by
#  13565 starred_actors
#  13130 written_by
#  12483 has_genre
#   9697 has_tags
#   3174 in_language
#    328 has_imdb_rating
#    122 has_imdb_votes
