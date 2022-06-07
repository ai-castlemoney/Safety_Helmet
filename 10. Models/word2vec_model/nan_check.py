from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import numpy as np

# 만들어진 Word2Vec 모델을 불러온다.
model = Word2Vec.load('Models/word2vec_model/final_data_mecab_ing_word2vec.model')
word_vectors = model.wv
vocabs = word_vectors.key_to_index.keys()

word_vectors_list = [word_vectors[v] for v in vocabs]
print(word_vectors_list[:5])