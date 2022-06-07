# 단어장과 vecter tsv 파일을 읽어서 사이킷런으로 코사인유사도 구하는 코드

# 필요한 라이브러리 임포트
import numpy as np
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
#from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity


# 파이어베이스 앱 이니셜라이즈
cred = credentials.Certificate('cloud_function/mykey.json')
app = firebase_admin.initialize_app(credential=cred, options=None, name='[DEFAULT]')

bucket = storage.bucket()
words_name = 'GJ&case_mecab_ing_word2vec_2_words_tsv.tsv'

blob = bucket.blob('model/'+words_name)
    #new token and metadata 설정
    # new_token = uuid4()
    # metadata = {"firebaseStorageDownloadTokens": new_token} #access token이 필요하다.
metadata = {"firebaseStorageDownloadTokens": '9eb7e5c6-38b3-4350-b4f2-2d096cbe7671'} #access token이 필요하다.
blob.metadata = metadata





#워드임배딩 백터 및 단어장 가져오기
vectors_path = '/Users/namcheolher/aiffel/Safety_Helmet/cloud_function/GJ&case_mecab_ing_word2vec_2_vectors_tsv.tsv'
words_path = '/Users/namcheolher/aiffel/Safety_Helmet/cloud_function/GJ&case_mecab_ing_word2vec_2_words_tsv.tsv'

vectors = pd.read_csv(vectors_path, sep= '\t')
vectors = vectors.to_numpy() # 임베딩 백터 넘파이로 변경
print(vectors.shape)
words = pd.read_csv(words_path, sep= '\t')

#print(vectors.head())
print(words.head())
print(words.columns)

# 단어 인덱스 사전 만들기
word2index = {v:k for k, v in words['0'].to_dict().items()}
# 단어2백터 사용 방법 : print(vectors[word2index[단어]])



# 입력값 sen2vec 으로
input_words = ['작업', '설치', '없는단어' ] # 입력예
input_vectors = np.array([vectors[word2index[word]] for word in input_words if word in word2index] )
#print(input_vectors)
input_sen2vec =np.nanmean(input_vectors,axis=0)
print('--------------')
print(input_sen2vec)

print('done')