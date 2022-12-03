from main import filtered_sentence
import pandas as pd

df_train = pd.read_csv('training_data.csv')
df_test = pd.read_csv('test_data.csv')

disease = df_train['prognosis'].tolist()