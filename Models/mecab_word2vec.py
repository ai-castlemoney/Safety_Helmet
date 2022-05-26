# 형태소 분석을 통해 토큰화가 진행
# Word2Vec(skip-gram) 벡터화 진행

from gensim.models import Word2Vec
from konlpy.tag import Mecab
import pandas as pd
import pprint
import re

# csv형태의 데이터를 불러온다.
data_path = 'Models/sample_data/train_GJ&case.csv'
data = pd.read_csv(data_path)

# 리스트 형식으로 데이터를 바꿔준다.
corpuses = []
for sentence in data['sentence']:
    corpuses.append(sentence)
    #print(sentence)

def get_stopwords():
    stopwords = list()
    
    f = open('Models/sample_data/stopwords.txt', 'r', encoding='utf-8')
    
    while True:
        line = f.readline()
        if not line: break
        stopwords.append(line.strip())
        
    return stopwords

def meacb_tokenizer(corpuses):

    corpuses = [re.sub(r'[^ ㄱ-ㅣ가-힣A-Za-z]', '', corpus) for corpus in corpuses]   # 특수기호, 한자 제거
    mecab = Mecab(dicpath=r"C:/Users/김민주/mecab/mecab-ko-dic")
    answer = []
    for corpus in corpuses:
        temp =[]
        stopwords = get_stopwords()   # 불용어 처리
        for token in mecab.nouns(corpus):
            if token not in stopwords and len(token)>1:
                temp.append(token)
        answer.append(temp)
    return answer

mecab_word2vec_model = Word2Vec(meacb_tokenizer(corpuses), epochs=10, vector_size=300, window=3, min_count = 5, workers=4, sg=1)
mecab_word2vec_model.save('Models/word2vec_model/GJ&case_mecab_word2vec.model')

word_vectors = mecab_word2vec_model.wv

vocabs = list(word_vectors.index_to_key)
word_vectors_list = [word_vectors[v] for v in vocabs] 

#pprint.pprint(word_vectors_list[:5]) # 벡터화 결과

