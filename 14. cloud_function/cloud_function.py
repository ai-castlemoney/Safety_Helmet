# 단어장과 vecter tsv 파일을 읽어서 사이킷런으로 코사인유사도 구하는 코드
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

vectors_path = '/Users/namcheolher/aiffel/Safety_Helmet/cloud_function/GJ&case_mecab_ing_word2vec_2_vectors_tsv.tsv'
words_path = '/Users/namcheolher/aiffel/Safety_Helmet/cloud_function/GJ&case_mecab_ing_word2vec_2_words_tsv.tsv'

vectors = pd.read_csv(vectors_path, sep= '\t')
vectors = vectors.to_numpy()
print(vectors.shape)
words = pd.read_csv(words_path, sep= '\t')

#print(vectors.head())
print(words.head())
print(words.columns)

# 단어 인덱스 사전 만들기
word2index = {v:k for k, v in words['0'].to_dict().items()}
print(vectors[word2index['작업']]+ vectors[word2index['설치']])
# print(word2index[''])


# 입력값 sen2vec 으로
input_words = ['작업', '설치', '없는단어' ] # 입력예
input_vectors = np.array([vectors[word2index[word]] for word in input_words if word in word2index] )
#print(input_vectors)
input_sen2vec =np.nanmean(input_vectors,axis=0)
print('--------------')
print(input_sen2vec)


print('done')