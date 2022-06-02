import numpy as np
import pandas as pd


# csv 파일 불러오기
data_path = 'Models_2/data/final_data_copy_r1.csv'

# data의 id 컬럼
data = pd.read_csv(data_path)
data_id = data['id']
#print(len(data_id))

# 규정 길이 : 7593
# 사고사례 600 길이 : 602
# 사고사례 10000 길이 : 11919
GJ_id = data_id[:7592+1]
#print(len(GJ_id))
#print(GJ_id.tail(3))
case600_id = data_id[7593:8194+1]
#print(case600_id.tail(3))
#print(len(case600_id))
case10000_id = data_id[8195:]
#print(case10000_id.tail(3))
#print(len(case10000_id))

GJ_id.to_csv("C:/Users/김민주/project/Safety_Helmet/Models_2/data/GJ_id.csv", index = False)
case600_id.to_csv("C:/Users/김민주/project/Safety_Helmet/Models_2/data/case600_id.csv", index = False)
case10000_id.to_csv("C:/Users/김민주/project/Safety_Helmet/Models_2/data/case10000_id.csv", index = False)

print("Done to save :)")