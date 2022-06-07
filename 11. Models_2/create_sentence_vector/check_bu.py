# 단어 벡터가 생성된 모델을 사용한다.

from gensim.models import Word2Vec
from konlpy.tag import Mecab
import pandas as pd
import numpy as np
import re

data_path = 'Models_2/data/final_data.csv'
data = pd.read_csv(data_path)
data_sentence = data['sentence']
#print(data_sentence)

corpuses = []
for sentence in data_sentence:
    corpuses.append(sentence)
#print(corpuses[:3], len(corpuses))

# a = 생성된 단어장 크기 확인
def meacb_tokenizer(corpuses):
    corpuses = [re.sub(r'[^ ㄱ-ㅣ가-힣A-Za-z]', '', corpus) for corpus in corpuses]   # 특수기호, 한자 제거
    mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")
    answer = []
    a = 0
    for corpus in corpuses:
        temp =[]
        a += len(mecab.nouns(corpus))
        #print(a)
        for token in mecab.nouns(corpus):
            temp.append(token)
        answer.append(temp)
    return answer


# # 문장 벡터 평균 구하기
# # 주어진 문장(단어 리스트)에서 단어 벡터의 평균을 구하는 함수
# def makeFeatureVec(words, model, num_features):
#     # 속도를 위해 0으로 채운 배열로 초기화 한다.
#     featureVec = np.zeros((num_features,),dtype="float32")

#     nwords = 0.
#     # Index2word는 모델의 사전에 있는 단어명을 담은 리스트이다.
#     # 속도를 위해 set 형태로 초기화 한다.
#     corpus_index2word = model.wv.index_to_key
#     # 루프를 돌며 모델 사전에 포함이 되는 단어라면 피처에 추가한다.

#     for word in words:
#         #print(word)
#         if word in corpus_index2word:
#             nwords = nwords + 1.
#             featureVec = np.add(featureVec,model.wv[word])
#     # 결과를 단어수로 나누어 평균을 구한다.

#     featureVec = np.divide(featureVec,nwords)

#     return featureVec
answer = meacb_tokenizer([corpuses[0]])
print(answer)
print(corpuses)
print('-----------')
print()
print(corpuses[10353:10356])
answer = meacb_tokenizer(corpuses[10353:10356])
print(answer)
print('-----------')
# print('?',corpuses[10354])
# answer = meacb_tokenizer(corpuses[10354])
# print(answer)
# print('-----------')
# answer = meacb_tokenizer(corpuses[10355])
# print(answer)
#print(answer[:3])

# ################################
# vectors_path = 'C:/Users/김민주/project/Safety_Helmet/Models_2/word2vec_model/final_data_vectors_tsv.tsv'
# words_path = 'C:/Users/김민주/project/Safety_Helmet/Models_2/word2vec_model/final_data_words_tsv.tsv'

# vectors = pd.read_csv(vectors_path, sep= '\t')
# vectors = vectors.to_numpy()
# print(vectors.shape)
# words = pd.read_csv(words_path, sep= '\t')

# #print(vectors.head())
# print(words.head())
# print(words.columns)

# # 단어 인덱스 사전 만들기
# word2index = {v:k for k, v in words['0'].to_dict().items()}
# print(vectors[word2index['작업']]+ vectors[word2index['설치']])
# print(word2index[''])


# # 입력값 sen2vec 으로
# input_words = ['작업', '설치', '없는단어' ] # 입력예
# input_vectors = np.array([vectors[word2index[word]] for word in input_words if word in word2index] )
# print(input_vectors.shape)
# input_sen2vec =np.nanmean(input_vectors,axis=0)
# print('--------------')
# print(input_sen2vec.shape)

# answer = [['작업', '설치', '없는단어' ], ['작업', '없는단어' ]]
# import warnings
# with warnings.catch_warnings():
#     warnings.simplefilter("ignore", category=RuntimeWarning)
#     sentence_vector = []
#     for sentence in answer:
#         input_words = sentence # 입력예
#         input_vectors = np.array([vectors[word2index[word]] for word in input_words if word in word2index] )
#         # print(input_vectors.shape)
#         input_sen2vec =np.nanmean(input_vectors, axis=0)
#         # print(input_sen2vec.shape)
#         sentence_vector.append(input_sen2vec)
#         result_np = np.array(sentence_vector)
#         print('차원', result_np.shape)

# print('----------------')
# result_np = np.array(sentence_vector)



# # # # 예상 shape : (20116, 300)
# print('차원', result_np.shape)
# np.save('Models_2/create_sentence_vector/final_data_sentence_vector_nanmean.npy', result_np)

