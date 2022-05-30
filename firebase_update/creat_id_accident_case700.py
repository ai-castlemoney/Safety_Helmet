from lib2to3.pgen2.pgen import DFAState
import pandas as pd
df = pd.read_csv('/Users/namcheolher/aiffel/Safety_Helmet/firebase_update/data/test_preprocessing2 copy.csv')
df.insert(0,'id','')
df.insert(3,'title_sentence','')
df['title_sentence'] = df[['title', 'sentence']].apply(lambda row: ','.join(row.values.astype(str)), axis=1)


for i in range(len(df)):
    id_i = '{0:05d}'.format(i)
    df['id'][i] = id_i


df.to_csv('/Users/namcheolher/aiffel/Safety_Helmet/firebase_update/DB_firebase/DB_id_accident_case_601.csv')
print(df.head())
print(df.tail())