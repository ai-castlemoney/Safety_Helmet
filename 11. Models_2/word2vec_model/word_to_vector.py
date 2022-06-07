# 사용자 정의 단어사전 mecab 사용 (사용자 정의 단어사전 완료)
# Word2Vec(skip-gram) 벡터화 진행
from cmath import nan
from gensim.models.callbacks import CallbackAny2Vec
from gensim.models import Word2Vec
from konlpy.tag import Mecab
import pandas as pd
import re


# 리스트 형식으로 데이터를 바꿔준다.
# 빈 문자열 행을 삭제한 데이터로 진행
data_path = 'Models_2/data/final_data_copy_r1.csv'
data = pd.read_csv(data_path)
data_sentence = data['sentence']

corpuses = []
for sentence in data_sentence:
    corpuses.append(sentence)

# for corpus in corpuses:
#     print('전:',corpus)
#     corpus = [re.sub(r'[^ ㄱ-ㅣ가-힣A-Za-z]', '', corpus)]
#     print('후:',corpus)


# mecab을 사용하여 단어(명사)들을 뽑아온다.
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
# 단어들이 300차원으로 임베딩된다.
mecab_word2vec_model = Word2Vec(meacb_tokenizer(corpuses), epochs=128, vector_size=300, window=10, min_count=3, workers=4, sg=1, compute_loss=True, callbacks=[callback()])
mecab_word2vec_model.save('Models_2/word2vec_model/final_data_word2vec_nantest.model')

print('done :)')