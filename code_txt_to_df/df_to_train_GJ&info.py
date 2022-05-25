# 완성된 Db 데이터 프레임을 학습에 활용할 데이터 셋으로 변환하는 코드
import numpy as np
import pandas as pd
import os
import csv

# 함수들

# 경로의 파일 모두 읽기
def load_dfs(read_dir):
    dir_list = os.listdir(read_dir) # 읽기 경로의 파일들
    #print(dir_list)
    dfs_list = []
    for txt_name in dir_list:
        print(txt_name)
        txt_path = read_dir + '/' + txt_name
        df = pd.read_csv(txt_path)
        dfs_list.append(df)
    dfs = pd.concat(dfs_list)
    dfs = dfs.reset_index(drop=True)
    return dfs

def dfs_to_trainDF(dfs):
    dfs = dfs.replace(np.nan,'',regex=True)
    train_data_list = []
    for i in range(len(dfs)):
        if dfs['group'][i]=='m' and ((dfs['title_category'][i] =='규정' or dfs['content_category'][i] =='규정') or (dfs['title_category'][i] =='정보' or dfs['content_category'][i] =='정보')):
            if dfs['title'][i] and dfs['content'][i]:
                temp = dfs['title'][i] + '\n' + dfs['content'][i]
            elif dfs['title'][i]:
                temp = dfs['title'][i]
            elif dfs['content'][i]:
                temp = dfs['content'][i]
            else:
                pass
            train_data_list.append(temp)
        elif dfs['group'][i]=='s' and ((dfs['title_category'][i] =='규정' or dfs['content_category'][i] =='규정') or (dfs['title_category'][i] =='정보' or dfs['content_category'][i] =='정보')):
            if dfs['title'][i] and dfs['content'][i]:
                train_data_list[-1] += '\n' + str(dfs['title'][i]) + '\n' +str(dfs['content'][i])
            elif dfs['title'][i]:
                train_data_list[-1] += '\n' + str(dfs['title'][i])
            elif dfs['content'][i]:
                train_data_list[-1] += '\n' +str(dfs['content'][i])
            else:
                pass
        else:
            pass
    return train_data_list

def train_DF_to_csv(train_DF, save_dir):
    file_name = 'tf_idf_train_GJ&info.csv'
    with open(save_dir+'/'+file_name, 'w') as file: 
        writer = csv.writer(file) 
        writer.writerow(train_DF)
    return "done"






# 메인

## 읽기 경로
read_dir = "/Users/namcheolher/aiffel/Safety_Helmet/add_MS_Column/csv"
save_dir = '/Users/namcheolher/aiffel/Safety_Helmet/code_txt_to_df/db_df_result'

dfs = load_dfs(read_dir)
#print(dfs)
print('Df 길이',len(dfs))
#print(str(NaN))

train_DF = dfs_to_trainDF(dfs)
#print(train_DF)
print('train_DF 길이',len(train_DF))
train_DF_to_csv(train_DF, save_dir)