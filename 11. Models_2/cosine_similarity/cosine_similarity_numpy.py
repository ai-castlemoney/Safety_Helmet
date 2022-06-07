from gensim.models import Word2Vec
import numpy as np
import pandas as pd

# input으로 받는 단어들
input_words = ['조경', '이식', '이동식크레인', '조경수', '충전전로', '전선', '전봇대', '맨홀', '벽', '고압선', '고소']

# input으로 받은 단어들의 평균 벡터(문장벡터)를 구하는 함수
def makeFeatureVec(input_words):
    # 사용할 word2vec model을 불러온다.
    model = Word2Vec.load('C:/Users/김민주/project/Safety_Helmet/Models_2/word2vec_model/final_data_word2vec_nantest.model')
    # Index2word는 모델의 사전에 있는 단어명을 담은 리스트이다.
    corpus_index2word = model.wv.index_to_key
    # input 단어들의 벡터 구하기
    input_vectors = np.array([model.wv[word] for word in input_words if word in corpus_index2word])
    # 단어벡터의 평균
    input_sen2vec =np.nanmean(input_vectors, axis=0)

    return input_sen2vec

words_vector = makeFeatureVec(input_words)
words_vector = words_vector.reshape(1, -1)

# 규정, 600, 10000의 sentence_vector 불러오기
case600_vector = np.load('Models_2/create_sentence_vector/sentence_vector_final_r1_case600.npy')
case10000_vector = np.load('Models_2/create_sentence_vector/sentence_vector_final_r1_case10000.npy')
GJ_vector = np.load('Models_2/create_sentence_vector/sentence_vector_final_r1_GJ.npy')
# print(case600_vector.shape)
# print(case10000_vector.shape)
# print(GJ_vector.shape)

# 코사인 유사도 측정하는 함수 생성
# input_words : 입력 단어들의 벡터
# vector : 규정, 사고사례 600, 10000 벡터
def getSentenceVector(input_words, vector):
    cosine_similarity = []
    for vector_ in vector:
        score = np.dot(input_words, vector_) / (np.linalg.norm(input_words) * (np.linalg.norm(vector_)))
        cosine_similarity.append(score)
    return np.array(cosine_similarity).reshape(1, -1)

# 각각의 sentence_vector와 코사인 유사도 실행
cosine_sim_600 = getSentenceVector(words_vector, case600_vector)        # input으로 받은 words와 case600()과 비교
cosine_sim_10000 = getSentenceVector(words_vector, case10000_vector)
cosine_sim_GJ = getSentenceVector(words_vector, GJ_vector)
# print(cosine_sim_600.shape)
# print(cosine_sim_10000.shape)
# print(cosine_sim_GJ.shape)

## step 1 : index와 코사인 유사도 값이 튜플로 묶인 리스트 생성
sim600_scores = list(enumerate(cosine_sim_600[0]))
sim10000_scores = list(enumerate(cosine_sim_10000[0]))
simGJ_scores = list(enumerate(cosine_sim_GJ[0]))

## step 2 : 코사인 유사도 값(x[1])을 기준으로 리스트 정렬
sim600_scores = sorted(sim600_scores, key=lambda x: x[1], reverse=True)
sim10000_scores = sorted(sim10000_scores, key=lambda x: x[1], reverse=True)
simGJ_scores = sorted(simGJ_scores, key=lambda x: x[1], reverse=True)
# print('정렬 후 :', sim600_scores)

## step 3 : 정렬된 리스트에서 상위 3개만 가져온다.
case600_top3 = sim600_scores[:3]
case10000_top3 = sim10000_scores[:3]
GJ_top3 = simGJ_scores[:10]
# print(case600_top3)
# print(case10000_top3)
# print(GJ_top3)

## step 4 : 졍렬된 리스트에서 idx를 사용해 문장의 id를 가져온다.
## 1. 상위 3개의 인덱스 받아오기
case600_top3_idx = [idx[0] for idx in case600_top3]
case10000_top3_idx = [idx[0] for idx in case10000_top3]
GJ_top3_idx = [idx[0] for idx in GJ_top3]
## 2. 받아온 인덱스를 사용해 id 가져오기
## 1) case 600
case600_id_path = 'Models_2/data/case600_id.csv'
case600_id = pd.read_csv(case600_id_path)
print(case600_id.iloc[case600_top3_idx])
## 2) case 10000
case10000_id_path = 'Models_2/data/case10000_id.csv'
case10000_id = pd.read_csv(case10000_id_path)
print(case10000_id.iloc[case10000_top3_idx])
## 3) GJ
GJ_id_path = 'Models_2/data/GJ_id.csv'
GJ_id = pd.read_csv(GJ_id_path)
print(GJ_id.iloc[GJ_top3_idx])