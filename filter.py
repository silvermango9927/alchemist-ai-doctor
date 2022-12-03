from main import filtered_sentence
from sklearn.metrics.pairwise import cosine_similarity # Cosine similarity techniques are used to easily assess the similarity and relevance of the frames of the video with the query
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df_train = pd.read_csv('training_data.csv')
df_test = pd.read_csv('test_data.csv')

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
highestSymptom = ""
for i in range(len(filtered_sentence)):
        for j in range(len(disease_column)):
                a = cosine_similarity([lis_embeddings[i]], [dis_embeddings[j]])
                if (a[0][0] >= 0.8):
                        if (a[0][0] > maxNum):
                                maxNum = a[0][0]
                                highestSymptom = disease_column[j]
                                # print(f" {disease_column[j]}: {a}: {filtered_sentence[i]}")
        if highestSymptom not in symptoms: symptoms.append(highestSymptom)

print(symptoms)
# for i in filtered_sentence:
#    x=TfidVectoriser().fit_transform([i])
#    for v in disease_column:
#         y=TfidVectoriser().fit_transform([v])
#         cosine_similarities = cosine_similarity(x, y)
#         print(f"{i}: {cosine_similarities} :{v}")
#         best_match_index = cosine_similarities.argmax()