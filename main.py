import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from sklearn.metrics.pairwise import cosine_similarity # Cosine similarity techniques are used to easily assess the similarity and relevance of the frames of the video with the query
import pandas as pd
from nltk.corpus import wordnet
from sentence_transformers import SentenceTransformer
import wikipedia
from summarizer import TransformerSummarizer


nltk.download('punkt')

df_train = pd.read_csv('training_data.csv')
df_test = pd.read_csv('test_data.csv')

df_train = df_train.drop('malaise', axis=1)
df_test = df_test.drop('malaise', axis=1)

disease = df_train['prognosis'].tolist()
disease_column = list(df_train.columns.values)
disease_column = [i.replace('_', ' ') for i in disease_column]

model = SentenceTransformer('bert-base-nli-mean-tokens')
dis_embeddings = model.encode(disease_column)


def runFunc(data):
    line = data
    line = line.translate(str.maketrans('', '', string.punctuation))

    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(line)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_sentence = ' '.join(filtered_sentence).split()

    symptoms = []
    maxNum = 0

    
    synsymptoms = []


    for i in filtered_sentence:
            for syn in wordnet.synsets(i):
                    for lm in syn.lemmas():
                            synsymptoms.append(lm.name())
    lis_embeddings1 = model.encode(synsymptoms)

    highestSymptom = ""

    for i in range(len(synsymptoms)):
            for j in range(len(disease_column)):
                    a = cosine_similarity([lis_embeddings1[i]], [dis_embeddings[j]])
                    if (a[0][0] >= 0.8):
                            if (a[0][0] > maxNum):
                                    maxNum = a[0][0]
                                    highestSymptom = disease_column[j]
            if highestSymptom not in symptoms: symptoms.append(highestSymptom)
    symptoms = [i for i in symptoms if i]
    print(symptoms)

    df_new = df_test

    for index, row in df_new.iterrows():
        for i in symptoms:
            if row[i.replace(' ', '_')] == 0:
                df_new = df_new[df_new.index != index]
    finalDiagnosis = list(df_new['prognosis'])
    # content = wikipedia.page(df_new['prognosis'])
    # GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")
    # gpt_summary = ''.join(GPT2_model(content.content, num_sentences=4))
    return finalDiagnosis