import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')

line = "I have itching, throat irritation, vomiting, nausea, and high fever"
line = line.translate(str.maketrans('', '', string.punctuation))

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(line)
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
print(filtered_sentence)