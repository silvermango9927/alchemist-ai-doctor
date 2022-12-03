from filter import a, disease_column, df_train, df_test, symptoms
from main import filtered_sentence
import pandas as pd

# for i in symptoms:
#     d = df_test.loc[df_train[i.replace(' ', '_')] == 1]
#     print(d)

print(symptoms)
#dick = {}
#for i in disease_column:
#    if i in symptoms:
#        dick.update({i:1})
#    else:
#        dick.update({i:0})
#val = df_train.lookup(list(dick), cols)
#l=pd.merge(pd.Series(dick), df_train, how='inner')
#print(l)
#for k in symptoms:
#    df = df.loc[(df[key] == column_value_pairs[key])]