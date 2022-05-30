import numpy as np
import pandas as pd
import os
import csv

# 경로의 파일 모두 읽기
def load_dfs(read_dir):
    dir_list = os.listdir(read_dir) # 읽기 경로의 파일들
    print(len(dir_list))
    dfs_list = []
    for txt_name in dir_list:
        #print(txt_name)
        txt_path = read_dir + '/' + txt_name
        df = pd.read_csv(txt_path)
        dfs_list.append(df)
    dfs = pd.concat(dfs_list)
    dfs = dfs.reset_index(drop=True)
    return dfs

def train_DF_to_csv(train_DF, save_dir):
    file_name = 'DB_id_GJ.csv'
    train_DF.to_csv(save_dir+'/'+file_name)
    return "done"


# 메인

## 읽기 경로
read_dir = "/Users/namcheolher/aiffel/Safety_Helmet/add_MS_Column/csv"
save_dir = '/Users/namcheolher/aiffel/Safety_Helmet/firebase_update/DB_firebase'

dfs = load_dfs(read_dir)
dfs = dfs.replace(np.nan,'',regex=True)
dfs.rename(columns={'Unnamed: 0':'id'}, inplace= True)
cols = ['doc_code', 't1', 't2', 't3', 't4', 'c1', 'c2', 'c3','c4']
dfs['id'] = dfs[cols].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
dfs['id'] = dfs['id'].replace("__",'_',regex=True)
dfs['id'] = dfs['id'].replace("__",'_',regex=True)
dfs['id'] = dfs['id'].replace("__",'_',regex=True)
dfs['id'] = dfs.apply(lambda x : x['id'][:-1] 
                    if x['id'].endswith('_') 
                    else x['id'] , axis=1)
# sentence 컬럼 추가
dfs.insert(2,'sentence','')
dfs.insert(3,'ref','')
cols = ['image', 'picture', 'table', 'appendix', 'math_exp', 'attachment',
       'reference', 'enclosure_image', 'enclosure', 'asterisk',
       'appendix_table']
dfs['ref'] = dfs[cols].apply(lambda row: ','.join(row.values.astype(str)), axis=1)
dfs['ref'] = dfs['ref'].replace(",,",',',regex=True)
dfs['ref'] = dfs['ref'].replace(",,",',',regex=True)
dfs['ref'] = dfs['ref'].replace(",,",',',regex=True)
dfs['ref'] = dfs['ref'].replace(",,",',',regex=True)
dfs['ref'] = dfs['ref'].replace(",,",',',regex=True)

print(len(dfs))
print(dfs.head())

for i in range(len(dfs)):
    dfs['content_category'][i] = str(dfs['title_category'][i]) + str(dfs['content_category'][i])
    if dfs['group'][i]=='m':
        c = 1
        if dfs['title'][i] and dfs['content'][i]:
            dfs['sentence'][i] = dfs['title'][i] + '\n' + dfs['content'][i]
        elif dfs['title'][i]:
            dfs['sentence'][i] = dfs['title'][i]
        elif dfs['content'][i]:
            dfs['sentence'][i] = dfs['content'][i]
        else:
            pass
    elif dfs['group'][i]=='s':
        if dfs['title'][i] and dfs['content'][i]:
            dfs['sentence'][i-c] += '\n' + str(dfs['title'][i]) + '\n' +str(dfs['content'][i])
        elif dfs['title'][i]:
            dfs['sentence'][i-c] += '\n' + str(dfs['title'][i])
        elif dfs['content'][i]:
            dfs['sentence'][i-c] += '\n' +str(dfs['content'][i])
        else:
            pass
        dfs['ref'][i-c] += ',' + dfs['ref'][i]
        c += 1
    else:
        if dfs['title'][i] and dfs['content'][i]:
            dfs['sentence'][i] = dfs['title'][i] + '\n' + dfs['content'][i]
        elif dfs['title'][i]:
            dfs['sentence'][i] = dfs['title'][i]
        elif dfs['content'][i]:
            dfs['sentence'][i] = dfs['content'][i]
        else:
            pass


print(len(dfs[dfs['group']!='s']))
new_dfs = dfs[dfs['group']!='s']
new_dfs = new_dfs[['id', 'doc_code','content_category','group', 'sentence','ref']]
new_dfs.rename(columns={'content_category':'category'}, inplace= True)

new_dfs['ref'] = new_dfs['ref'].replace(",,",',',regex=True)
new_dfs['ref'] = new_dfs['ref'].replace(",,",',',regex=True)
new_dfs['ref'] = new_dfs['ref'].replace(",,",',',regex=True)
new_dfs['ref'] = new_dfs['ref'].replace(",,",',',regex=True)
new_dfs['ref'] = new_dfs['ref'].replace(",,",',',regex=True)
new_dfs['ref'] = new_dfs['ref'].replace(", ",',',regex=True)

# for i in range(len(new_dfs)):
#     new_dfs['sentence'][i] = sentence_list[i]
#     new_dfs['ref'][i] = appendix_list[i]
print(new_dfs.head())
dfs_sort_id = new_dfs.sort_values(by=new_dfs.columns[1])
dfs_sort_id.reset_index(drop=True, inplace=True)
print(dfs_sort_id.head())
#print(dfs_sort_id['id'][760],dfs_sort_id['id'][761])
#dfs_sort_id['id'][0] = 'C-09-2012_6.0_6.1_(11)'
#dfs_sort_id['doc_code'][0] = 'C-09-2012'
dfs_sort_id = dfs_sort_id.sort_values(by=dfs_sort_id.columns[0])
dfs_sort_id.reset_index(drop=True, inplace=True)

for i in range(len(dfs_sort_id)):
    if dfs_sort_id['ref'][i].endswith(','):
        dfs_sort_id['ref'][i] = dfs_sort_id['ref'][i][:-1]
    if dfs_sort_id['ref'][i].startswith(','):
        dfs_sort_id['ref'][i] = dfs_sort_id['ref'][i][1:]

print(dfs_sort_id.head())

dfs_sort_id = dfs_sort_id.drop(dfs_sort_id.index[0])
dfs_sort_id.reset_index(drop=True, inplace=True)
dfs_sort_id['category'] = dfs_sort_id['category'].replace("_x0008_",'',regex=True)
print(dfs_sort_id[dfs_sort_id['category']==''])

print(len(dfs_sort_id))
print(dfs_sort_id.head())

print(dfs_sort_id['category'].unique())

train_DF_to_csv(dfs_sort_id, save_dir)