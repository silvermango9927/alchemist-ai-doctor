from main import filtered_sentence
from sklearn.metrics.pairwise import cosine_similarity # Cosine similarity techniques are used to easily assess the similarity and relevance of the frames of the video with the query
import pandas as pd
from nltk.corpus import wordnet


df_train = pd.read_csv('training_data.csv')
df_test = pd.read_csv('test_data.csv')

df_train = df_train.drop('malaise', axis=1)
df_test = df_test.drop('malaise', axis=1)

disease = df_train['prognosis'].tolist()
disease_column = list(df_train.columns.values)
disease_column = [i.replace('_', ' ') for i in disease_column]

symptoms = []
maxNum = 0

from sentence_transformers import SentenceTransformer
model = SentenceTransformer('bert-base-nli-mean-tokens')
dis_embeddings = model.encode(disease_column)
# print(disease_column)
# print(filtered_sentence)
lis_embeddings = model.encode(filtered_sentence)
bleh = []

for i in filtered_sentence:
        for syn in wordnet.synsets(i):
                for lm in syn.lemmas():
                        bleh.append(lm.name())
lis_embeddings1 = model.encode(bleh)
highestSymptom = ""
for i in range(len(bleh)):
        for j in range(len(disease_column)):
                a = cosine_similarity([lis_embeddings1[i]], [dis_embeddings[j]])
                if (a[0][0] >= 0.8):
                        if (a[0][0] > maxNum):
                                maxNum = a[0][0]
                                highestSymptom = disease_column[j]
        if highestSymptom not in symptoms: symptoms.append(highestSymptom)
symptoms = [i for i in symptoms if i]
print(symptoms)