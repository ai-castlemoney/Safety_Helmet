# 1. EDA_컬럼분할, 제거.csv파일을 firebase DB 로 업데이트 하는 코드

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
update_db = pd.read_csv('/Users/namcheolher/aiffel/Safety_Helmet/firebase_update/DB_firebase/DB_id_accident_case_10000.csv', index_col = 0)
update_db.reset_index(drop=True, inplace=True)
# update_db.to_csv('/Users/namcheolher/aiffel/Safety_Helmet/firebase_update/DB_firebase/DB_id_accident_case_10000.csv')
print(update_db.columns)
print(update_db.head())
print(update_db.tail())
# Use the application default credentials

cred = credentials.Certificate('/Users/namcheolher/aiffel/Safety_Helmet/firebase_update/mykey.json') # 키 경로
app = firebase_admin.initialize_app(credential=cred, options=None, name='[DEFAULT]')
# 업데이트

db = firestore.client()
for i in range(len(update_db)):
    doc_ref = db.collection('accident_case').document(str(update_db['id'][i]))
    doc_ref.set({
        'id': str(update_db['id'][i]),
        'title': str(update_db['사고명'][i]),
        'sequence': str(update_db['사고경위'][i]),
        'cause': str(update_db['사고원인'][i]),
        'cause_detail': str(update_db['구체적 사고원인'][i]),
        'dead': str(update_db['사망자수'][i]),
        'injured': str(update_db['부상자수'][i]),
    })
    print(i)

#

firebase_admin.delete_app(app)

# Index(['사고명', '기상상태', '시설물 종류', '인적사고', '물적사고', '작업프로세스', '사고경위', '사고원인',
#        '구체적 사고원인', '사망자수', '부상자수', '공종대분류', '공종소분류', '객체대분류', '객체소분류', '시설장소',
#        '위치장소', '부위위치'],
#       dtype='object')