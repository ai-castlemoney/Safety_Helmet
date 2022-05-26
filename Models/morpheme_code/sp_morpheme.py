import pandas as pd
import urllib.request
import csv
import sentencepiece as spm

# data 불러오기
data_path = 'Models/sample_data/train_GJ&case.csv'
data = pd.read_csv(data_path)

# sentencepiece에 넣어주기 위해 txt파일로 변환
with open('GJ&case_sentence.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(data['sentence']))

# input : 학습시킬 파일
# model_prefix : 만들어질 모델 이름
# vocab_size : 단어 집합의 크기
# model_type : 사용할 모델(unigram(default), bpe, char, word)
# max_sentence_length : 문장의 최대 길이
# pad_id,pad_piece : pad token id,  값
# unk_id, unk_piece : unknown token id, 값
# bos_id, bos_piece : begin of sentence token id, 값
# eos_id, eos_piece : end of sequence token id, 값
# user_defined_symbols : 사용자 정의 토큰
spm.SentencePieceTrainer.Train(
    f"--input=GJ&case_sentence.txt --model_prefix=GJ&case_8000 --vocab_size=8000" + 
    "--model_type=unigram" + 
    " --max_sentence_length=999999" +  # 문장 최대 길이
    " --pad_id=0 --pad_piece=[PAD]" +  # pad token 및 id 지정
    " --unk_id=1 --unk_piece=[UNK]" +  # unknown token 및 id 지정
    " --bos_id=2 --bos_piece=[BOS]" +  # begin of sequence token 및 id 지정
    " --eos_id=3 --eos_piece=[EOS]" +  # end of sequence token 및 id 지정
    " --user_defined_symbols=[SEP],[CLS],[MASK]" +  # 기타 추가 토큰 SEP: 4, CLS: 5, MASK: 6
    " --input_sentence_size=100000" +  # 말뭉치에서 샘플링해서 학습
    " --shuffle_input_sentence=true")  # 샘플링한 말뭉치 shuffle

vocab_list = pd.read_csv('GJ&case_8000.vocab', sep='\t', header=None, quoting=csv.QUOTE_NONE)
vocab_list.to_csv("Models/create_vocabulary/GJ&case_8000_vocabulary.csv")
print(vocab_list)
print(len(vocab_list))