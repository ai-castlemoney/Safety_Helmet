# append 순서 : 규정 + 601 + 10000

import pandas as pd

# 규정 id
data_GJ_path = 'firebase_update/DB_firebase/DB_id_GJ.csv'
data_GJ = pd.read_csv(data_GJ_path)
data_GJ_id = data_GJ['id']

# 601 id
data_601_path = 'firebase_update/DB_firebase/DB_id_accident_case_601.csv'
data_601 = pd.read_csv(data_601_path)
data_601_id = data_601['id']

# 10000 id
# 사고사례 10000은 id 부여가 되어있지 않음.
# data_10000_path = 'firebase_update/DB_firebase/DB_id_accident_case_10000.csv'
# data_10000 = pd.read_csv(data_10000_path)
# data_10000_id = data_10000['id']

id_before = data_GJ_id.append(data_601_id)
print(id_before)
print(len(id_before))
df_id = pd.DataFrame(id_before, columns = 'id')
# id_final = id_before.append(data_10000_id)
# print(id_final)
# print(len(id_final))

data_path = 'Models/final_data.csv'
data = pd.read_csv(data_path)
df = pd.DataFrame(data)

df.loc[:,'id'] = df_id
