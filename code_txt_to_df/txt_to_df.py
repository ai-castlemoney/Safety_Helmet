# txt_preprocessing_r2 의 txt를 df의 테이블 형태로 변환 하는 코드

# 참고 기준

# r2 의 기준
# # 1. 그림 저장
# - 폴더명 : C-01-2011
# - 파일명 : ex. <그림 1>, <표 1>
#     - 그림 2개를 한 번에 캡쳐할 경우, <그림 1_2>와 같이 파일명 추가

# # 2. 텍스트 수정

# - ‘ - ‘ 앞 뒤로 띄어쓰기 1개가 있어야 함
# - txt 파일에는 그림 <그림 1> 추가 기재
# - 그림 2개가 캡쳐되어있는 경우 텍스트를 <그림 1_2>로 기재

# 라이브러리
import os
import pandas as pd
import re

# 파일 하나 읽기
def load_txt(txt_path):
    doc_code = txt_path.split('.')[-2].split('/')[-1]
    with open(txt_path,'r') as txt_data:
        txt = txt_data.readlines()
    txts = {doc_code:txt}
    return txts
# 경로의 파일 모두 읽기
def load_txts(read_dir):
    
    dir_list = os.listdir(read_dir) # 읽기 경로의 파일들
    txts = {}
    for txt_name in dir_list:

        print(txt_name)
        doc_code = txt_name.split(".")[0]
        txt_path = read_dir +'/' + txt_name

        with open(txt_path,'r') as txt_data:
            txt = txt_data.readlines() # lines 는 각 문장이 리스트로 들어간다.
        txts[doc_code] = txt
    return txts

# 각 문서 txt를 df에 추가
def txt_to_df(doc_code, txt):
    cols = ["doc_code", "t1", "t2", "t3", "c1", "c2", "c3", "c4", "title", "content", "image", "table", "appendix"]
    #Create a DataFrame object
    df = pd.DataFrame(columns = cols)
    new_row = {
        "doc_code" : doc_code,
        "t1" : None,
        "t2" : None,
        "t3" : None,
        "c1" : None,
        "c2" : None,
        "c3" : None,
        "c4" : None,
        "title" : None,
        "content" : None,
        "image" : None,
        "table" : None,
        "appendix" : None}

    # t1~3, c1~4 정규표현식
    t1 = re.compile('^\d+[.] ')
    t2 = re.compile('^\d+[.]\d+ ')
    t3 = re.compile('^\d+[.]\d+[.]\d+ ')
    c1 = re.compile('^[(]\d+[)] ')
    c2 = re.compile('^[(][가-하][)] ')
    c3 = re.compile('^[①-⑳] ')
    c4 = re.compile('^[①-⑳] ')

    for line in txt: # 각 문장에 대해서
        line_splitted = line.split()
        col_type = line_splitted[0]
        data = " ".join(line_splitted[1:])

        print(col_type)
    print(df)
    return df

txt_path = "txt_preprocessing_r2/C-01-2011.txt"
txts = load_txt(txt_path)

# df 초기화
cols = ["doc_code", "t1", "t2", "t3", "c1", "c2", "c3", "c4", "title", "content", "image", "table", "appendix"]
    #Create a DataFrame object
    df = pd.DataFrame(columns = cols)
    new_row = {
        "doc_code" : doc_code,
        "t1" : None,
        "t2" : None,
        "t3" : None,
        "c1" : None,
        "c2" : None,
        "c3" : None,
        "c4" : None,
        "title" : None,
        "content" : None,
        "image" : None,
        "table" : None,
        "appendix" : None}
for doc_code, txt in txts.items():
    txt_to_df(doc_code, txt)


# Get file names in dir
read_dir = 'hackerthon/읽기 경로'
save_dir = 'hackerthon/저장 경로'
#dir_list.remove('.DS_Store') # mac.os 의 ds_store 파일 제거