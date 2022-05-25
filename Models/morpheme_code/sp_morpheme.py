# csv 데이터를 리스트로 불러온다.
import pandas as pd
import urllib.request
import csv
import sentencepiece as spm

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

with open('accidentcase_sentence.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(data['sentence']))

# input : 학습시킬 파일
# model_prefix : 만들어질 모델 이름
# vocab_size : 단어 집합의 크기
# model_type : 사용할 모델(unigram(default), bpe, char, word)
# max_sentence_length : 문장의 최대 길이
# pad_id,pad_piece : pad token id, 값
# unk_id, unk_piece : unknown token id, 값
# bos_id, bos_piece : begin of sentence token id, 값
# eos_id, eos_piece : end of sequence token id, 값
# user_defined_symbols : 사용자 정의 토큰
spm.SentencePieceTrainer.Train('--input=accidentcase_sentence.txt --model_prefix=accidentcase_unigram --vocab_size=9900 --model_type=unigram --max_sentence_length=9999')

vocab_list = pd.read_csv('accidentcase_unigram.vocab', sep='\t', header=None, quoting=csv.QUOTE_NONE)
vocab_list.to_csv("C:/Users/김민주/project/Safety_Helmet/TF_IDF_test/create_vocabulary/accidentcase_sp_unigram_vocabulary.csv")
print(vocab_list)