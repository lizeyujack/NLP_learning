# NLP_learning
Learning for dealing data in Application studio A course, UTS

Firstly, I need to review some useful libraries like "numpy" "NLTK" and "word" 

[![GitHub top language](https://img.shields.io/github/languages/top/lizeyujack/NLP_learning?style=plastic)](https://www.udemy.com/course/nlp-tangyudi/learn/lecture/13816460#overview)
[![GitHub followers](https://img.shields.io/github/followers/lizeyujack?style=social)](https://github.com/lizeyujack?tab=followers)
***
[class 7: video link](https://www.udemy.com/course/nlp-tangyudi/learn/lecture/13816464#overview)
```py
import re
from nltk.corpus import stopwords
s = '   ab  cd ^888 https://gitlab.com/nlp_ericsson_spring/nlp_ericsson2/-/tree/zeyu'
# select the specific stopwords corpus
cache_english_stopwords = stopwords.words('english')

# remove the links
text = re.sub(r'https:\/\/[a-z]*\.[a-z]*\/[a-z]*\_[a-z]*\_[a-z]*\/[a-z]*\_[a-z]*[0-9]\/\-\/[a-z]*\/[a-z]*','............',s)
print(text)

```
```shell
Python - data_clearn.py:8
   ab  cd ^888 ............
[Finished in 1.048s]
```
