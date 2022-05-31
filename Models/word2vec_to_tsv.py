# Word2Vec으로 만들어진 모델을 tsv파일로 변환
from gensim.models import Word2Vec
import pandas as pd

# mecab을 사용한 모델 
model_path = 'C:/Users/김민주/project/Safety_Helmet/Models/word2vec_model/GJ&case_mecab_ing_word2vec_2.model'

model = Word2Vec.load(model_path)
df = pd.DataFrame(model.wv.vectors)
df2 = pd.DataFrame(model.wv.index_to_key)

df.to_csv('Models/word2vec_model/GJ&case_mecab_ing_word2vec_2_vectors_tsv.tsv', sep = '\t', index = False)
df2.to_csv('Models/word2vec_model/GJ&case_mecab_ing_word2vec_2_words_tsv.tsv', sep = '\t', index = False)

print('Done :)')