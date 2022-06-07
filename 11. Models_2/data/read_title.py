import pandas as pd

data = pd.read_csv('Models_2/user_mecab_vocab/title.csv', names=['doc_num', 'title'])
print(data)