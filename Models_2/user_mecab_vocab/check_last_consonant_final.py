# csv 파일을 읽어서 종성을 확인하고 종성 컬럼에 
# 참고 : https://github.com/letsgo247/under-checker/blob/master/%EB%B0%9B%EC%B9%A8%20%ED%8C%90%EB%8B%A8%EA%B8%B0.py
import pandas as pd
   
def check_last_consonant(word):    #아스키(ASCII) 코드 공식에 따라 입력된 단어의 마지막 글자 받침 유무를 판단해서 뒤에 붙는 조사를 리턴하는 함수
    last = word[-1]     #입력된 word의 마지막 글자를 선택해서
    criteria = (ord(last) - 44032) % 28     #아스키(ASCII) 코드 공식에 따라 계산 (계산법은 다음 포스팅을 참고하였습니다 : http://gpgstudy.com/forum/viewtopic.php?p=45059#p45059)
    if 'a' <= last <= "z" or 'A' <= last <='Z': # 알파벳인 경우 F
        return 'F'
    if criteria == 0:       #나머지가 0이면 받침이 없는 것
        return 'F'
    else:                   #나머지가 0이 아니면 받침 있는 것
        return 'T'

read_dir = 'Models_2/user_mecab_vocab/user_vocab.csv' # csv 읽을 경로
save_dir = 'Models_2/user_mecab_vocab/user_vocab_tf.csv' # 처리후 csv 저장 경로

df = pd.read_csv(read_dir, encoding='utf-8')
#print(df.columns)
col_TF = 'T_F' # 받침유무를 넣을 컬럼명
col_word = 'word' # 받침을 확인할 단어컬럼
for i in range(len(df)):
    df[col_TF][i] = check_last_consonant(df[col_word][i])
    #print(df[col_TF][i],df[col_word][i])


df.to_csv(save_dir, encoding='utf-8')
# print(check_last_consonant('한글'))
# print(check_last_consonant('새우'))
# print(check_last_consonant('LPG'))
# print(check_last_consonant('sdc'))

