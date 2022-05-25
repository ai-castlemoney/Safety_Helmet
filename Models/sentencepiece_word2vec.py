# 형태소 분석을 통해 토큰화가 진행
# Word2Vec(skip-gram) 벡터화 진행

from gensim.models import Word2Vec
import sentencepiece as spm
import pandas as pd
import pprint
import re

# csv형태의 데이터를 불러온다.
data_path = 'Models/sample_data/accident_train_sample.csv'
data = pd.read_csv(data_path)

# 리스트 형식으로 데이터를 바꿔준다.
corpuses = []
for sentence in data['sentence']:
    corpuses.append(sentence)

# Word2Vec를 사용해 백터화를 진행한다.
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

def sp_tokenizer(corpuses):
    
    corpuses = [re.sub(r'[^ ㄱ-ㅣ가-힣]', '', corpus) for corpus in corpuses] # 특수기호, 영어, 한자 제거
    sp = spm.SentencePieceProcessor()
    vocab_file = "Models/sentencepiece/accidentcase_unigram.model"
    sp.load(vocab_file)
    answer = []
    for corpus in corpuses:
        temp =[]
        for token in sp.encode_as_pieces(corpus):
            temp.append(token)
        answer.append(temp)    
    return answer

sp_word2vec_model = Word2Vec(sp_tokenizer(corpuses), epochs=5, vector_size=300, window=3, min_count = 5, workers=4, sg=1)

sp_word2vec_model.save('C:/Users/김민주/project/Safety_Helmet/Models/word2vec_model/sp_word2vec_model.model')
word_vectors = sp_word2vec_model.wv

vocabs = list(word_vectors.index_to_key)
word_vectors_list = [word_vectors[v] for v in vocabs]  

#pprint.pprint(word_vectors_list[:5]) # 벡터화 결과