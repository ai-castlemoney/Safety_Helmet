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
update_db = pd.read_csv('/Users/namcheolher/aiffel/Safety_Helmet/firebase_update/DB_firebase/DB_id_accident_case_700.csv',
                    index_col=0,
                    dtype = {'id': str})
#update_db.reset_index(drop=True, inplace=True)
print(update_db.columns)
print(update_db.head())
print(update_db.tail())



# Use the application default credentials

cred = credentials.Certificate('/Users/namcheolher/aiffel/Safety_Helmet/firebase_update/mykey.json') # 키 경로
app = firebase_admin.initialize_app(credential=cred, options=None, name='[DEFAULT]')
# 업데이트

db = firestore.client()
for i in range(len(update_db)):

    doc_ref = db.collection('accident_case_700').document(update_db['id'][i])
    doc_ref.set({
        'title': str(update_db['title'][i]),
        'sentence': str(update_db['sentence'][i]),
    })
    print(i)
    # if i ==5:
    #     break

#

firebase_admin.delete_app(app)