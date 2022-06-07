#-*- coding:utf-8 -*-
# sklearn을 사용한 코사인 유사도 측정

from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
from konlpy.tag import Mecab
import numpy as np
import re

data_sentence =['구성 및 특성\r\n시스템폼은 기본적으로 2개 이상의 브라켓 유니트로 이루어져 있다. 상부 작업대(0레벨) 중간작업대(-1레벨), 하부작업대(-2레벨), 거푸집 및 콘크리트 타설용 발판(+1레벨)로 구성되어 있다.\r\n상부작업대(0레벨)은 거푸집 아래에 있는 작업발판이고 클라이밍 시스템의 메인 크로스빔이 있는 0레벨 발판이며 거푸집 해체·설치가 이루어진다.\r\n중간작업대(-1레벨)는 거푸집의 인양작업 발판이고 하부작업대(-2레벨)는 거푸집 인양 후 슈(Shoe) 제거작업, 마감작업 등을 위한 발판이고 +1레벨 발판을 통상적으로 콘크리트 타설용으로 거푸집에 설치되어 있다.\r\nRCS 레일은 보통 2개 이상의 클라이밍 레일로 이루어져 있고 각각의 레일은 클라이밍 레일 커플링으로 연결되어 -1레벨의 헤비 듀티 스핀들을 이용해서 거푸집 인양을 위한 각도를 조절할 수 있다.\r\n모든 브라켓유니트가 연결된 클라이밍 레일은 M20볼트에 의해 클라이밍 슈 걸림쇠에 지지되며 클라이밍 슈는 월슈 또는 슬라브슈에 연결되어 하중 을 전달하고 월슈 및 슬라브슈는 M24볼트나 M30볼트로 콘크리트 타설시 미리 매립되어 있는 클라이밍 콘과 타이로드, 앵커플레이트에 연결되어 하중을 구조체로 전달한다.\r\n시스템폼의 모든 구성 부재 및 부속품은 제작사의 정품을 사용하고 안전성을 확인 하여야 한다. ']

corpuses = []
for sentence in data_sentence:
    corpuses.append(sentence)
print(corpuses, len(corpuses))


# 1. input 문장의 token화
# 한 줄의 문장이 들어가는 것을 가정
def meacb_tokenizer(corpuses):
    corpuses =[ re.sub(r'[^ ㄱ-ㅣ가-힣A-Za-z]', '', corpus)  for corpus in corpuses]   # 특수기호, 한자 제거
    mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")
    # answer = [mecab.nouns(corpuses)]
    answer = []
    for corpus in corpuses:
        temp =[]
        for token in mecab.nouns(corpus):
            temp.append(token)
        answer.append(temp)
    return answer


# 2. input의 단어벡터 생성
# vector_size, window, sg만 설정. 나머지는 defult값 사용
input_word2vec_model = Word2Vec.load('Models/word2vec_model/final_data_mecab_ing_word2vec.model')

# 3. input의 문장벡터 생성
def makeFeatureVec(words, model, num_features):
    # 속도를 위해 0으로 채운 배열로 초기화 한다.
    featureVec = np.zeros((num_features,),dtype="float32")

    nwords = 0.
    # Index2word는 모델의 사전에 있는 단어명을 담은 리스트이다.
    corpus_index2word = model.wv.index_to_key
    # 루프를 돌며 모델 사전에 포함이 되는 단어라면 피처에 추가한다.
    for word in words:
        #print(word)
        if word in corpus_index2word:
            nwords = nwords + 1.
            #print(np.add(featureVec,model.wv[word]))
            featureVec = np.add(featureVec,model.wv[word])
    # 결과를 단어수로 나누어 평균을 구한다.
    print(featureVec.shape, nwords)

    featureVec = np.divide(featureVec,nwords)
     
    return featureVec


sentence_vector = np.empty(shape=(300,1), dtype='float32')
model = Word2Vec.load('Models/word2vec_model/final_data_mecab_ing_word2vec.model')
for sentence in meacb_tokenizer(corpuses):
    
    sentence_vector = np.add(sentence_vector,makeFeatureVec(sentence, model, 300))
sentence_vector = np.transpose(sentence_vector)
# 저장되어 있는 sentence_vector 불러오기
vector_case600 = np.load('C:/Users/김민주/project/Safety_Helmet/Models/sentence_vector/case600_sentence_vector.npy')
vector_case10000 = np.load('C:/Users/김민주/project/Safety_Helmet/Models/sentence_vector/case10000_sentence_vector.npy')
vector_GJ = np.load('C:/Users/김민주/project/Safety_Helmet/Models/sentence_vector/GJ_sentence_vector.npy')

print(sentence_vector.shape)
print(vector_case600.shape)
print(vector_case10000.dtype)
print(vector_GJ.dtype)

# 각각의 sentence_vector와 코사인 유사도 실행
cosine_sim_600 = cosine_similarity(sentence_vector, vector_case600)
cosine_sim_10000 = cosine_similarity(sentence_vector, vector_case10000)
cosine_sim_GJ = cosine_similarity(sentence_vector, vector_GJ)


# 유사도에 따라 문장들 정렬?
# sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

# 가장 유사한 --개의 문장 받아오기
# sim_scores = sim_scores[1:11]


# vector_to_id?
