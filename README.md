# NLP_learning
Learning for dealing data in Application studio A course, UTS

Firstly, I need to review some useful libraries like "numpy" "NLTK" and "word" 

[![GitHub top language](https://img.shields.io/github/languages/top/lizeyujack/NLP_learning?style=plastic)](https://www.udemy.com/course/nlp-tangyudi/learn/lecture/13816460#overview)
[![GitHub followers](https://img.shields.io/github/followers/lizeyujack?style=social)](https://github.com/lizeyujack?tab=followers)
***
[class 7: video link](https://www.udemy.com/course/nlp-tangyudi/learn/lecture/13816464#overview)
## remove the hyperlink with '............' 
```py
import re
from nltk.corpus import stopwords
s = '   ab  cd ^888 https://gitlab.com/nlp_ericsson_spring/nlp_ericsson2/-/tree/zeyu'
# select the specific stopwords corpus
cache_english_stopwords = stopwords.words('english')

# remove the links
text = re.sub(r'https:\/\/\w+\.\w+\/\w+\_\w+\_\w+\/\w+\_\w+\/\-\/\w+\/\w+','............',s)
print(text)

```
result
```shell
Python - data_clearn.py:8
   ab  cd ^888 ............
[Finished in 1.048s]
```
## example for removing the "stopwords(meaningless words)"
```python
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
```
result
```shell
Python - data_clearn.py:3
I handsome beautiful boy ! !
[Finished in 1.168s]
```
