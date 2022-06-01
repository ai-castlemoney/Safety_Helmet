# 노션 5월 23일자 부분 단어벡터 출력 예시 참고

from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import numpy as np

model = Word2Vec.load('Models/word2vec_model/final_data_mecab_ing_word2vec.model')
word_vectors = model.wv
#vocabs = word_vectors.key_to_index.keys()
#word_vectors_list = [word_vectors[v] for v in vocabs]

word_1 = ['노무자','이헌','씨','수평','비계','체중','조인트','입','우측면','사고','수평','비계','체중','조인트','핀','발생']

word_2 = ['차량탑재형','크레인','톤','자재','작업발판','중','크레인','턴테이블','연결볼트','파단','분경','밑','작업','중','사고자',
'후','사고','발생','로','연락','건양','응급실','이송','시','분경','사망','사건','크레인','턴테이블','연결볼트','파단','자재','낙하','협착']

# word = list(set(word))
# word_1_vec = []
# for i in word_1:
#     try:
#         vocabs = word_vectors.get_vector(i, norm=True)
#         word_1_vec.append(vocabs)
#     except:
#         print(i)
# 
# result_word_1 = np.array(word_1_vec)
#print(len(vocabs))
#print(vocabs)

def makeFeatureVec(words, num_features):
    # 속도를 위해 0으로 채운 배열로 초기화 한다.
    featureVec = np.zeros((num_features,),dtype="float32")

    nwords = 0.
    # Index2word는 모델의 사전에 있는 단어명을 담은 리스트이다.
    # 속도를 위해 set 형태로 초기화 한다.
    corpus_index2word = model.wv.index_to_key
    # 루프를 돌며 모델 사전에 포함이 되는 단어라면 피처에 추가한다.

    for word in words:
        #print(word)
        if word in corpus_index2word:
            nwords = nwords + 1.
            featureVec = np.add(featureVec,model.wv[word])
    # 결과를 단어수로 나누어 평균을 구한다.

    featureVec = np.divide(featureVec,nwords)

    return featureVec

print(makeFeatureVec(word_1, 300))
print(makeFeatureVec(word_2, 300))