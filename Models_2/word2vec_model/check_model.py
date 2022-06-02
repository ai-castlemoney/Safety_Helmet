# 생성된 모델에 담긴 단어와 벡터를 확인한다.
# gensim 4.0.0 version github : https://github.com/RaRe-Technologies/gensim/wiki/Migrating-from-Gensim-3.x-to-4
# numpy nan 확인 : https://www.adamsmith.haus/python/answers/how-to-check-for-nan-elements-in-a-numpy-array-in-python

from gensim.models import Word2Vec
import numpy as np

# 만들어진 Word2Vec 모델을 불러온다.
model = Word2Vec.load('Models_2/word2vec_model/final_data_word2vec_nantest.model')
word_vectors = model.wv

# vocab : 모델에 저장되어 있는 단어(7785개) / dict_keys(['중', '작업', ..., '숯', '주초'])

vocabs = word_vectors.key_to_index.keys()
print(len(vocabs))
print(vocabs)

# word_vectors_list = [word_vectors[v] for v in vocabs]
# #print(word_vectors_list[:5])

# # 벡터가 들어있는 리스트를 넘파이 배열로 변환한다.
# word_vectors_np = np.array(word_vectors_list)

# # 넘파이 배열 안에 nan이 있는지 확인해본다. 
# array_sum = np.sum(word_vectors_np)
# check = np.isnan(array_sum)
# print(check)