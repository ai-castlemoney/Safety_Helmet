from gensim.models import Word2Vec
from konlpy.tag import Mecab
import pandas as pd
import pprint
import re

# csv형태의 데이터를 불러온다.
data_path = 'C:/Users/김민주/project/Safety_Helmet/firebase_update/DB_firebase/DB_id_accident_case_10000.csv'
data = pd.read_csv(data_path)

# 리스트 형식으로 데이터를 바꿔준다.
corpuses = []
for sentence in data['사고경위_구체적 사고원인']:
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
df.to_csv('Models/create_vocabulary/case_10000_mecab_words_nan.csv')
