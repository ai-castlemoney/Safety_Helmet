from konlpy.tag import Mecab
import pandas as pd
import re

# csv형태의 데이터를 불러온다.
data_path = 'Models_2/data/final_data.csv'
data = pd.read_csv(data_path)

# 리스트 형식으로 데이터를 바꿔준다.
corpuses = []
for sentence in data['sentence']:
    corpuses.append(sentence)
    #print(sentence)

# 문장에 대해 mecab을 적용하여 명사들만 가져온다.
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

answer = meacb_tokenizer(corpuses)

# 길이 확인
single_word = []
length = 0
for i in answer:
    print('문장길이 :', len(i))
    length += len(i)
    print('length :', length)
    for j in i:
        single_word.append(j)
print(len(single_word))
