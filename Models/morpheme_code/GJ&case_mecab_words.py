from gensim.models import Word2Vec
from konlpy.tag import Mecab
import pandas as pd
import pprint
import re

# csv형태의 데이터를 불러온다.
data_path = 'C:/Users/김민주/project/Safety_Helmet/Models/sample_data/train_GJ&case.csv'
data = pd.read_csv(data_path, encoding='cp949')

# 리스트 형식으로 데이터를 바꿔준다.
corpuses = []
for sentence in data['sentence']:
    corpuses.append(sentence)
    #print(sentence)

def meacb_tokenizer(corpuses):

    corpuses = [re.sub(r'[^ ㄱ-ㅣ가-힣A-Za-z]', '', corpus) for corpus in corpuses]   # 특수기호, 한자 제거
    mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")
    answer = []
    for corpus in corpuses:
        temp =[]
        for token in mecab.nouns(corpus):
            temp.append(token)
        answer.append(temp)
    return answer

# print(meacb_tokenizer(corpuses))

answer = meacb_tokenizer(corpuses)

df = pd.DataFrame(answer)
df.to_csv('Models/create_vocabulary/GJ&case_mecab_words2.csv')
