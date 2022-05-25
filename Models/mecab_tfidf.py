# 형태소 분석을 통해 토큰화가 진행
# TF-IDF 벡터화 진행

from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Mecab
import pickle
import pandas as pd
import pprint
import re

# csv형태의 데이터를 불러온다.
data_path = 'C:/Users/김민주/project/Safety_Helmet/Models/sample_data/accident_train_sample.csv'
data = pd.read_csv(data_path)

# 리스트 형식으로 데이터를 바꿔준다.
corpuses = []
for sentence in data['sentence']:
    corpuses.append(sentence)

# TF-IDF를 사용해 백터화를 진행한다.
# 이와 동시에 형태소 분석도 같이 진행한다.
#def get_stopwords():
#    stopwords = list()
#    
#    f = open('./stopwords.txt', 'r', encoding='utf-8')
#    
#    while True:
#        line = f.readline()
#        if not line: break
#        stopwords.append(line.strip())
#        
#    return stopwords

def meacb_tokenizer(corpuses):
    mecab = Mecab(dicpath=r"C:/Users/김민주/mecab/mecab-ko-dic")
    corpuses = re.sub(r'[^ ㄱ-ㅣ가-힣A-Za-z]', '', corpuses)   # 특수기호, 한자 제거
    return [token for token in mecab.nouns(corpuses) if len(token)>1]

vectorizer = TfidfVectorizer(tokenizer = meacb_tokenizer)
vectorizer.fit(corpuses)
matrix = vectorizer.transform(corpuses)

pprint.pprint(vectorizer.vocabulary_) # 단어 사전

pickle.dump(vectorizer.vocabulary_,open("Models/word2vec_model/mecab_tfidf_words.pkl","wb"))  # 단어 사전 저장(미실행)

pprint.pprint(matrix.toarray()) # 분석 결과