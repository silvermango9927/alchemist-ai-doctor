from filter import a, disease_column, df_train, df_test, symptoms
from main import filtered_sentence
import pandas as pd

# for i in symptoms:
#     d = df_test.loc[df_train[i.replace(' ', '_')] == 1]
#     print(d)

#print(symptoms)
#val = df_train.lookup(list(dick), cols)
#l=pd.merge(pd.Series(dick), df_train, how='inner')
#print(l)
# for k in range(len(symptoms)):
#     a = df_test[symptoms[k].replace(' ', '_')] == symptoms[k].replace(' ', '_')
#     pp = df_test.loc[a]
# print(pp)

#print(df_train.loc['vomiting'])

# for i,row in df_train.iterrows():
#     for symp in symptoms:
#         print(row[row[symp.replace(' ', '_')]==1])

df_new = df_test

for index, row in df_new.iterrows():
    for i in symptoms:
        if row[i.replace(' ', '_')] == 0:
            df_new = df_new[df_new.index != index]
print(df_new)