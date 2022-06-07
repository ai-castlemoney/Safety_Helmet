# 사용자 정의 단어사전 mecab 사용 (미완성 상태_22.05.30)
# Word2Vec(skip-gram) 벡터화 진행
from gensim.models.callbacks import CallbackAny2Vec
from gensim.models import Word2Vec
from konlpy.tag import Mecab
import pandas as pd
import pprint
import re

# 규정 및 사고사례 데이터 가져오기
# data_GJ_path = 'firebase_update/DB_firebase/DB_id_GJ.csv'
# data_case6_path = 'firebase_update/DB_firebase/DB_id_accident_case_601.csv'
# data_case100_path = 'firebase_update/DB_firebase/DB_id_accident_case_10000.csv'

# data_GJ = pd.read_csv(data_GJ_path)
# data_case6 = pd.read_csv(data_case6_path)
# data_case100 = pd.read_csv(data_case100_path)

# 불러온 3개 데이터를 하나로 합친다.
# data_GJ_sentence = data_GJ[data_GJ['group']=='m']['sentence']  # 데이터 중 m으로 묶인 부분만 가져오기
# data_case6_sentence = data_case6['title_sentence']
# data_case100_sentence = data_case100['사고경위_구체적 사고원인']

# data_GJ_sentence_df = pd.DataFrame(data_GJ_sentence)
#print(len(data_GJ_sentence_df))
# data_case6_sentence_df = pd.DataFrame(data_case6_sentence)
# data_case6_sentence_df.rename(columns = {'title_sentence':'sentence'},inplace=True)
#print(len(data_case7_sentence_df))
# data_case100_sentence_df = pd.DataFrame(data_case100_sentence)
# data_case100_sentence_df.rename(columns = {'사고경위_구체적 사고원인':'sentence'},inplace=True)
#print(len(data_case100_sentence_df))

# data_before = data_GJ_sentence_df.append(data_case6_sentence_df, ignore_index=True)
# data = data_before.append(data_case100_sentence_df, ignore_index=True)
#print(data)

# data.to_csv('C:/Users/김민주/project/Safety_Helmet/Models/final_data.csv')


# 리스트 형식으로 데이터를 바꿔준다.
data_path = 'Models/final_data.csv'
data = pd.read_csv(data_path)
data_sentence = data['sentence']

corpuses = []
for sentence in data_sentence:
    corpuses.append(sentence)
    #print(sentence)

# a = 생성된 단어장 크기 확인
def meacb_tokenizer(corpuses):
    corpuses = [re.sub(r'[^ ㄱ-ㅣ가-힣A-Za-z]', '', corpus) for corpus in corpuses]   # 특수기호, 한자 제거
    mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")
    answer = []
    a = 0
    for corpus in corpuses:
        temp =[]
        a += len(mecab.nouns(corpus))
        #print(a)
        for token in mecab.nouns(corpus):
            temp.append(token)
        answer.append(temp)
    return answer

#answer, a = meacb_tokenizer(corpuses)
#print(a)

# unique 값만 모아놓은 단어장 크기 확인
#list_word = []
#for i in answer:
#    for j in i:
#        list_word.append(j)
#
#size_words = list(set(list_word))
#print(len(size_words))

# epoch 당 loss 확인
class callback(CallbackAny2Vec):
    """Callback to print loss after each epoch."""

    def __init__(self):
        self.epoch = 0
        self.loss_to_be_subed = 0

    def on_epoch_end(self, model):
        loss = model.get_latest_training_loss()
        loss_now = loss - self.loss_to_be_subed
        self.loss_to_be_subed = loss
        print('Loss after epoch {}: {}'.format(self.epoch, loss_now))
        self.epoch += 1


# 모델 생성
mecab_word2vec_model = Word2Vec(meacb_tokenizer(corpuses), epochs=128, vector_size=300, window=10, min_count=3, workers=4, sg=1, compute_loss=True, callbacks=[callback()])
mecab_word2vec_model.save('Models/word2vec_model/final_data_mecab_ing_word2vec.model')
print('done :)')


# word_vectors = mecab_word2vec_model.wv
# vocabs = list(word_vectors.index_to_key)
# word_vectors_list = [word_vectors[v] for v in vocabs] 