# 단어장을 만들어봅시다 :)
# 불용어를 걸러냅시다 :)

import csv
from collections import Counter
from konlpy.tag import Mecab
import numpy as np
import pandas as pd

# csv 데이터를 리스트로 불러온다.
data_path = 'Models/sample_data/train_GJ&case.csv'
data = pd.read_csv(data_path)

#data = []

#f = open(data_path,'r',encoding='utf-8')
#rea = csv.reader(f)

#for row in rea:
#    data.append(row)
#f.close

#data = data[0]
#data = pd.DataFrame(data, columns = ['sentence'])


# 단어장 생성
tokenizer = Mecab(dicpath=r"C:/Users/김민주/mecab/mecab-ko-dic")

# stopwords: 불용어
#def get_stopwords():
#    stopwords = list()
#    
#    f = open('Models/sample_data/stopwords.txt', 'r', encoding='utf-8')
#    
#    while True:
#        line = f.readline()
#        if not line: break
#        stopwords.append(line.strip())
#        
#    return stopwords

def load_data(data, num_words=10000):
    #data['sentence'] = str(data['sentence'])
    #data.drop_duplicates(subset=['sentence'], inplace=True)
    #data = data.dropna(how = 'any')
    data['sentence'] = data['sentence'].str.replace("[^.ㄱ-ㅎㅏ-ㅣ가-힣A-Za-z]"," ")
    clean_data = []
    for sentence in data['sentence']:
        temp_X = tokenizer.nouns(sentence) # 토큰화
        #print(temp_X)
        temp_X = [word for word in temp_X if len(word) > 1] # 불용어 제거
        clean_data.append(temp_X)
    
    # 단어 사전
    # <BOS>: 문장의 시작지점, <PAD>: 패딩용 단어, <UNK>: 사전에 없는(Unknown) 단어
    words = np.concatenate(clean_data).tolist()
    counter = Counter(words)
    counter = counter.most_common(15000-4)
    vocab = ['<PAD>', '<BOS>', '<UNK>', '<UNUSED>'] + [key for key, _ in counter]
    word_to_index = {word:index for index, word in enumerate(vocab)}  # {단어:숫자} 딕셔너리 구조
    
    # 텍스트를 단어 사전 인덱스로 변환하는 함수
    def wordlist_to_indexlist(wordlist):
        return [word_to_index[word] if word in word_to_index else word_to_index['<UNK>'] for word in wordlist]
        
    clean_data = list(map(wordlist_to_indexlist, clean_data))
        
    return clean_data, word_to_index

done_data, word_to_index = load_data(data)


# {숫자:단어}의 index_to_word 단어 사전 생성
index_to_word = {index:word for word, index in word_to_index.items()}

print(index_to_word)

df = pd.DataFrame(list(index_to_word.values()), columns=['word'])

df.to_csv("Models/create_vocabulary/GJ&case_mecab(sw)nouns_vocabulary.csv")

print("Done :)")