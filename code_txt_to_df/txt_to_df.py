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
    print(dir_list)
    txts = {}
    for txt_name in dir_list:
        print(txt_name)
        doc_code = txt_name.split(".")[0]
        txt_path = read_dir +'/' + txt_name
        with open(txt_path,'r') as txt_data:
            txt = txt_data.readlines() # lines 는 각 문장이 리스트로 들어간다.
        txts[doc_code] = txt
    return txts

def get_col_type(line_head, cols):

    t1 = re.compile('\d+[.]') # title 1 : 1.
    t2 = re.compile('\d+[.]\d+') # title 2 : 1.1
    t3 = re.compile('\d+[.]\d+[.]\d+') # title 3 : 1.1.1
    t4 = re.compile('\d+[.]\d+[.]\d+[.]\d+') # title 4 : 1.1.1.1
    c1 = re.compile('[(]\d+[)]') # content 1 : (1)~
    c2 = re.compile('[(][가-힣][)]') # content 2 : (가)~(힣)
    c3 = re.compile('[①-⑳]') # content 3 : ①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳
    c4 = re.compile('[㉮-㉻]') # content 4  : ㉮㉯㉰㉱㉲㉳㉴㉵㉶㉷㉸㉹㉺㉻

    if t4.match(line_head):
        col_type = 't4'
    elif t3.match(line_head):
        col_type = "t3"
    elif t2.match(line_head):
        col_type = "t2"
    elif t1.match(line_head):
        col_type = "t1"
    elif c1.match(line_head):
        col_type = "c1"
    elif c2.match(line_head):
        col_type = "c2"
    elif c3.match(line_head):
        col_type = "c3"
    elif c4.match(line_head):
        col_type = "c4"
    elif line_head == '-':
        col_type = '-'
    elif line_head == '그림':
        col_type = 'image'
    elif line_head == '표':
        col_type = "table"
    elif line_head == '부록':
        col_type = 'appendix'
    elif line_head == '수식':
        col_type = 'math_exp'
    elif line_head == '붙임':
        col_type = 'attachment'
    elif line_head == '참고':
        col_type = 'reference'
    elif line_head == '별지_그림':
        col_type = 'enclosure_image'
    elif line_head == '별지':
        col_type = 'enclosure'
    elif line_head == '별표':
        col_type = 'asterisk'
    elif line_head == '부록_표':
        col_type = 'appendix_table'
    else:
        col_type = 'content'

    return col_type

# 수식, 붙임, 참고, 별지_그림, 별지, 별표, 부록_표
#     "math_exp",
#     "attachment",
#     "reference",
#     "enclosure_image",
#     "enclosure",
#     "asterisk",
#     'appendix_table']

# 각 문서 txt를 df에 추가
def txt_to_df(doc_code, txt, df, cols):
    # t1~4, c1~4 정규표현식
    new_row = { col_name : None for col_name in cols} # 추가할 행 초기화
    new_row["doc_code"] = doc_code # 문서코드 행에 추가

    for line in txt: # 각 문장에 대해서

        # 글머리, 내용을 분리
        
        line_splitted = line.split()
        if line:
            #print(doc_code,line)
            line_head = line_splitted[0] # 글머리
            data = " ".join(line_splitted[1:]) # 내용

            # 글머리로 부터 col_type 얻기
            col_type = get_col_type(line_head, cols)
            #print(line_head, col_type)
            # col_type 이 t#, c# 이외인 경우
            if col_type == "t1": # t1 의 경우
                new_row["t1"] = line_head
                new_row["t2"] = None
                new_row["t3"] = None
                new_row["t4"] = None
                new_row["c1"] = None
                new_row["c2"] = None
                new_row["c3"] = None
                new_row["c4"] = None
                new_row["title"] = data
            elif col_type == "t2": # t2 의 경우
                new_row["t2"] = line_head
                new_row["t3"] = None
                new_row["t4"] = None
                new_row["c1"] = None
                new_row["c2"] = None
                new_row["c3"] = None
                new_row["c4"] = None
                new_row["title"] = data
            elif col_type == "t3":
                new_row["t3"] = line_head
                new_row["t4"] = None
                new_row["c1"] = None
                new_row["c2"] = None
                new_row["c3"] = None
                new_row["c4"] = None
                new_row["title"] = data
            elif col_type == "t4":
                new_row["t4"] = line_head
                new_row["c1"] = None
                new_row["c2"] = None
                new_row["c3"] = None
                new_row["c4"] = None
                new_row["title"] = data
            elif col_type == "c1":
                new_row["c1"] = line_head
                new_row["c2"] = None
                new_row["c3"] = None
                new_row["c4"] = None
                new_row["content"] = data
            elif col_type == "c2":
                new_row["c2"] = line_head
                new_row["c3"] = None
                new_row["c4"] = None
                new_row["content"] = data
            elif col_type == "c3":
                new_row["c3"] = line_head
                new_row["c4"] = None
                new_row["content"] = data
            elif col_type == "c4":
                new_row["c4"] = line_head
                new_row["content"] = data
            elif col_type == "-":
                if pre_col_type == "t1":
                    new_row["t2"] = line_head
                    new_row["t3"] = None
                    new_row["t4"] = None
                    new_row["c1"] = None
                    new_row["c2"] = None
                    new_row["c3"] = None
                    new_row["c4"] = None
                    new_row["title"] = data
                elif pre_col_type == "t2":
                    new_row["t3"] = line_head
                    new_row["t4"] = None
                    new_row["c1"] = None
                    new_row["c2"] = None
                    new_row["c3"] = None
                    new_row["c4"] = None
                    new_row["title"] = data
                elif pre_col_type == "t3":
                    new_row["t4"] = line_head
                    new_row["c1"] = None
                    new_row["c2"] = None
                    new_row["c3"] = None
                    new_row["c4"] = None
                    new_row["content"] = data
                elif pre_col_type == "t4":
                    new_row["c1"] = line_head
                    new_row["c2"] = None
                    new_row["c3"] = None
                    new_row["c4"] = None
                    new_row["content"] = data
                elif pre_col_type == "c1":
                    new_row["c2"] = line_head
                    new_row["c3"] = None
                    new_row["c4"] = None
                    new_row["content"] = data
                elif pre_col_type == "c2":
                    new_row["c3"] = line_head
                    new_row["c4"] = None
                    new_row["content"] = data
                elif pre_col_type == "c3":
                    new_row["c4"] = line_head
                    new_row["content"] = data
                else:
                    pass
            # col_type 이 그림 표 부록 등 이전행에 추가될 자료, 이전 행에 추가 후 다음 반복으로(continue)
            ## 바로 내용이 나오는 content 도 마찬가지.
            elif col_type in ["content","image","table","appendix","math_exp","attachment","reference","enclosure_image","enclosure","asterisk",'appendix_table']:
                # df 마지막 행의 [col_type] = data
                #print(df.iloc[-1][col_type])
                #print('여기?')
                if df.iloc[-1][col_type] != None : # 기존에 항목이 있으면 ", data"를 추가
                    df.iloc[-1][col_type] = df.iloc[-1][col_type] + ", " + data
                else:
                    df.iloc[-1][col_type] = data
                continue

            else:
                print(col_type, data, "어디에도 속하지 않습니다.")
                pass

            # new_row를 df 마지막에 추가
            new_df = pd.DataFrame([new_row])
            df = pd.concat([df,new_df],ignore_index=True)
            #df = df.append(new_row, ignore_index=True)


            # t#, c# 을 제외하고 new_row 초기화
            for col_name in ["title","content","image","table","appendix","math_exp","attachment","reference","enclosure_image","enclosure","asterisk",'appendix_table']:
                new_row[col_name] = None
                
            #print(line_head, col_type)
            # pre_col_type 복제
            pre_col_type = col_type
        else:
            pass
    #print(df)
    return df

#----------------- MAIN ---------------------#  

# df 초기화, 사용할 컬럼명 지정 
# 차례로 문서코드, 제목1~3, 내용1~4, 제목, 내용, 그림, 표, 부록, 수식, 붙임, 참고, 별지_그림, 별지, 별표, 부록_표
cols = [
    "doc_code",
    "t1",
    "t2",
    "t3",
    "t4",
    "c1",
    "c2",
    "c3",
    "c4",
    "title",
    "content",
    "image",
    "table",
    "appendix",
    "math_exp",
    "attachment",
    "reference",
    "enclosure_image",
    "enclosure",
    "asterisk",
    'appendix_table']

# #Create a DataFrame object
# df = pd.DataFrame(columns = cols)
# new_row = { col_name : None for col_name in cols} # 추가할 행 초기화
# #df = df.append(new_row, ignore_index=True)
# new_df = pd.DataFrame([new_row])
# df = pd.concat([df,new_df])
# print("concat done")

# 하나만 할 경우
txt_path = "txt_preprocessing_r2/C-01-2011.txt"
txts = load_txt(txt_path)

# 경로의 모든 파일에 대하여
read_dir = '/Users/namcheolher/aiffel/Safety_Helmet/code_txt_to_df/txt_r2'
txts = load_txts(read_dir)

# 확인
print(txts)
# 저장경로
save_dir = '/Users/namcheolher/aiffel/Safety_Helmet/code_txt_to_df/txt_to_df'
for doc_code, txt in txts.items(): # 각 문서에 대하여
    #df 초기화
    df = pd.DataFrame(columns = cols)
    print(doc_code," 이 문서를 txt to df작업중")
    # df  변환
    df = txt_to_df(doc_code, txt, df, cols)

    # 저장
    df.to_csv(save_dir+'/'+doc_code+'.csv', index=False)



# Get file names in dir
read_dir = 'hackerthon/읽기 경로'
save_dir = 'hackerthon/저장 경로'
#dir_list.remove('.DS_Store') # mac.os 의 ds_store 파일 제거