# append 순서 : 규정 + 601 + 10000

import pandas as pd

# 규정 및 사고사례 데이터 가져오기
data_GJ_path = 'firebase_update/DB_firebase/DB_id_GJ.csv'
data_case6_path = 'firebase_update/DB_firebase/DB_id_accident_case_601.csv'
data_case100_path = 'firebase_update/DB_firebase/DB_id_accident_case_10000.csv'

data_GJ = pd.read_csv(data_GJ_path)
data_case6 = pd.read_csv(data_case6_path)
data_case100 = pd.read_csv(data_case100_path)

# 불러온 3개 데이터에서 내용만 가져오기
data_GJ_sentence_id =  pd.DataFrame(data_GJ[data_GJ['group']=='m'][['id','sentence']])  # 데이터 중 m으로 묶인 부분만 가져오기
print(data_GJ_sentence_id)
# data_GJ_sentence_id.to_csv('data_GJ_sentence_id.csv')

data_case6_sentence_id =  pd.DataFrame(data_case6[['id','title_sentence']])
print(data_case6_sentence_id)

data_case100_sentence_id =  pd.DataFrame(data_case100[['id','사고경위_구체적 사고원인']])
print(data_case100_sentence_id)


data_case6_sentence_id.rename(columns = {'title_sentence':'sentence'},inplace=True)   # sentence로 column rename

data_case100_sentence_id.rename(columns = {'사고경위_구체적 사고원인':'sentence'},inplace=True)   # sentence로 column rename

sentence_before = data_GJ_sentence_id.append(data_case6_sentence_id, ignore_index=True)
sentence_after = sentence_before.append(data_case100_sentence_id, ignore_index=True)

sentence_after.to_csv('C:/Users/김민주/project/Safety_Helmet/Models/final_data.csv')

# --------------------
# 불러온 3개 데이터에서 id만 가져오기
# data_GJ_id =  pd.DataFrame(data_GJ['id'])
# data_case6_id =  pd.DataFrame(data_case6['id'])
# data_case100_id =  pd.DataFrame(data_case100['id'])

# id_before = data_GJ_id.append(data_case6_id, ignore_index=True)
# id_after = id_before.append(data_case100_id, ignore_index=True)

# data = pd.concat([id_after, sentence_after], axis=1, ignore_index=True)


# print(data)
#data.to_csv('C:/Users/김민주/project/Safety_Helmet/Models/final_data.csv')
