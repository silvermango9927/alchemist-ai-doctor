import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')

line = "I have rashes, nausea and red spots all over"
line = line.translate(str.maketrans('', '', string.punctuation))

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(line)
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
filtered_sentence = [i for i in filtered_sentence if not i == '']