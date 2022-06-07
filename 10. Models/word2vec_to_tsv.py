# Word2Vec으로 만들어진 모델을 tsv파일로 변환
from gensim.models import Word2Vec
import pandas as pd

# mecab을 사용한 모델 
model_path = 'C:/Users/김민주/project/Safety_Helmet/Models_2/word2vec_model/final_data_word2vec_nantest.model'

model = Word2Vec.load(model_path)
df = pd.DataFrame(model.wv.vectors)
df2 = pd.DataFrame(model.wv.index_to_key)
save_path ='C:/Users/김민주/project/Safety_Helmet/Models_2/word2vec_model/'
df.to_csv(save_path +'final_nantest_data_vectors_tsv.tsv', sep = '\t', index = False)
df2.to_csv(save_path + 'final_nantest_data_words_tsv.tsv', sep = '\t', index = False)

print('Done :)')