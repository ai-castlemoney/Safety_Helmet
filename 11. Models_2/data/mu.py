# 삽입했던 한자 부분의 행 지우고
# 새로운 final_data 생성

import pandas as pd

path = 'Models_2/data/final_data_copy.csv'

data = pd.read_csv(path, index_col=0)
print(data.tail())
print(data.columns)

print(data[data['sentence']  == '無'])
#print(data[data['sentence'].map(len)  <= 5])

data = data.drop([data.index[10354], data.index[11308]])
print(data[data['sentence']  == '無'])
data.reset_index(inplace=True)
print(data.tail())

data.to_csv('Models_2/data/final_data_copy_r1.csv', index=False)
