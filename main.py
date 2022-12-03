import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')

line = "My skin is itching and has red dense rashes with my stomach sometimes hurting. I'm also kinda vomiting after meals"
line = line.translate(str.maketrans('', '', string.punctuation))

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(line)
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]