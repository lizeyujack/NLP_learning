import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
s = 'I am a very handsome beautiful boy!!'
# select the specific stopwords corpus
cache_english_stopwords = stopwords.words('english')
# feed s into tokens
tokens = word_tokenize(s)
#iteration with list to find all of the meaningful word and put it into the list.
list_no_stopwords = [i for i in tokens if i not in cache_english_stopwords]
#join these words together and make them looks like a sentence.
text = ' '.join(list_no_stopwords)
print(text)
