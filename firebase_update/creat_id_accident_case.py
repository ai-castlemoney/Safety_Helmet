from unicodedata import category
import numpy as np
import pandas as pd
import os
import csv
##
#pip install firebase-admin


# firebase init
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


#파일 읽어오기
update_db = pd.read_csv('/Users/namcheolher/aiffel/Safety_Helmet/accident_case/EDA_accdent_case/1. EDA_컬럼분할, 제거.csv', index_col = 0)
update_db.reset_index(drop=True, inplace=True)
update_db.insert(0,'id','')
update_db.insert(3,'사고경위_구체적 사고원인','')
update_db['사고경위_구체적 사고원인'] = update_db[['사고경위', '구체적 사고원인']].apply(lambda row: ', '.join(row.values.astype(str)), axis=1)
for i in range(len(update_db)):
    update_db['id'][i] = 'AC-A-' + '{0:05d}'.format(i)

print(update_db.columns)
print(update_db.head())
print(update_db.tail())

update_db.to_csv('/Users/namcheolher/aiffel/Safety_Helmet/firebase_update/DB_firebase/DB_id_accident_case_10000.csv')


# Index(['사고명', '기상상태', '시설물 종류', '인적사고', '물적사고', '작업프로세스', '사고경위', '사고원인',
#        '구체적 사고원인', '사망자수', '부상자수', '공종대분류', '공종소분류', '객체대분류', '객체소분류', '시설장소',
#        '위치장소', '부위위치'],
#       dtype='object')

# 사고사례 중 모델에 사용할 데이터
# - 공종
# - 사고 객체
# - 작업 프로세스
# - 사고 경위
# - 구체적 사고 원인

# - category : 공종 + 사고 객체 + 작업 프로세스
# - sentence : 사고경위 + 구체적 사고 원인