# 단어장을 만들어봅시다 :)
# 불용어를 걸러냅시다 :)

import csv
from collections import Counter
from konlpy.tag import Okt
import numpy as np
import pandas as pd

# csv 데이터를 리스트로 불러온다.
#data_path = 'C:/Users/김민주/project/Safety_Helmet/TF_IDF_test/tf_idf_train_sample.csv'

#data = []

#f = open(data_path,'r',encoding='utf-8')
#rea = csv.reader(f)

#for row in rea:
#    data.append(row)
#f.close

#data = data[0]
#data = pd.DataFrame(data, columns = ['sentence'])

data_path = 'C:/Users/김민주/project/Safety_Helmet/TF_IDF_test/sample_data/accident_train_sample.csv'
data = pd.read_csv(data_path)

# 단어장 생성
tokenizer = Okt()

# stopwords: 불용어
stopwords = [ ]

def load_data(data, num_words=10000):
    #data['sentence'] = str(data['sentence'])
    #data.drop_duplicates(subset=['sentence'], inplace=True)
    #data = data.dropna(how = 'any')
    
    clean_data = []
    for sentence in data['sentence']:
        temp_X = tokenizer.morphs(sentence) # 토큰화
        #print(temp_X)
        temp_X = [word for word in temp_X if not word in stopwords] # 불용어 제거
        clean_data.append(temp_X)
    
    # 단어 사전
    # <BOS>: 문장의 시작지점, <PAD>: 패딩용 단어, <UNK>: 사전에 없는(Unknown) 단어
    words = np.concatenate(clean_data).tolist()
    counter = Counter(words)
    counter = counter.most_common(10000-4)
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

df.to_csv("C:/Users/김민주/project/Safety_Helmet/TF_IDF_test/create_vocabulary/accicentcase_Okt_vocabulary.csv")

print("Done :)")