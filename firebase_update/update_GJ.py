# DB_firebase/DB_id_GJ.csv 파일을 firebase DB 로 업데이트 하는 코드

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
update_db = pd.read_csv('/Users/namcheolher/aiffel/Safety_Helmet/firebase_update/DB_firebase/DB_id_GJ.csv', index_col = 0)
print(update_db.columns)
print(update_db)
# Use the application default credentials

cred = credentials.Certificate('/Users/namcheolher/aiffel/Safety_Helmet/firebase_update/mykey.json') # 키 경로
app = firebase_admin.initialize_app(credential=cred, options=None, name='[DEFAULT]')
# 업데이트

db = firestore.client()
for i in range(len(update_db)):

    doc_ref = db.collection('kosha_guide').document('C').collection(update_db['doc_code'][i]).document(update_db['id'][i])
    doc_ref.set({
        'group': update_db['group'][i],
        'category': update_db['category'][i],
        'sentence': update_db['sentence'][i],
        'ref': update_db['ref'][i],
        'id': update_db['id'][i],
        'doc_code': update_db['doc_code'][i],
    })
#

firebase_admin.delete_app(app)