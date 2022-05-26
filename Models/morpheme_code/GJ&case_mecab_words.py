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

# print(meacb_tokenizer(corpuses))

answer = meacb_tokenizer(corpuses)

df = pd.DataFrame(answer)
df.to_csv('Models/create_vocabulary/GJ&case_mecab_words.csv')
