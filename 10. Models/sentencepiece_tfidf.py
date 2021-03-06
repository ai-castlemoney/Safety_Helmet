# 형태소 분석을 통해 토큰화가 진행
# TF-IDF 벡터화 진행

from sklearn.feature_extraction.text import TfidfVectorizer
import sentencepiece as spm
import pandas as pd
import pprint
import re

# csv형태의 데이터를 불러온다.
data_path = 'C:/Users/김민주/project/Safety_Helmet/TF_IDF_test/sample_data/accident_train_sample.csv'
data = pd.read_csv(data_path)

# 리스트 형식으로 데이터를 바꿔준다.
corpus = []
for sentence in data['sentence']:
    corpus.append(sentence)

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

def sp_tokenizer(text):
    sp = spm.SentencePieceProcessor()
    text = re.sub(r'[^ ㄱ-ㅣ가-힣A-Za-z]', '', text) # 특수기호, 한자 제거
    vocab_file = "TF_IDF_test/accidentcase_unigram.model"
    sp.load(vocab_file)
    #stopwords = get_stopwords() # 불용어
    return [token for token in sp.encode_as_pieces(text)]

vectorizer = TfidfVectorizer(tokenizer = sp_tokenizer)
vectorizer.fit(corpus)
matrix = vectorizer.transform(corpus)

pprint.pprint(vectorizer.vocabulary_) # 단어 사전
pprint.pprint(matrix.toarray()) # 분석 결과