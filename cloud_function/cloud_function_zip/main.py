def hello_rtdb(event, context):
    """Triggered by a change to a Firebase RTDB reference.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    resource_string = context.resource
    # print out the resource string that triggered the function
    print(f"Function triggered by change to: {resource_string}.")
    # now print out the entire event object
    print(str(event))
    # mykey 추가
    # 라이브러리 임포트
# firebase test
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import firestore
    from gensim.models import Word2Vec
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np
    import pandas as pd

# 작업허가서, 공장정보 읽어오기
# Use the application default credentials
    cred = credentials.Certificate('data/mykey.json')
    app = firebase_admin.initialize_app(credential=cred, options=None, name='[DEFAULT]')
    db = firestore.client()
    # permit_to_work /event['data']['work_id']는 work1 이된다. 하위 딕셔너리 {data_time:, facility:, keywords: } 가 된다.
    work_id = str(eval(str(event))['data']['work_id'])
    doc_ref = db.collection(u'permit_to_work').document(work_id)
    doc = doc_ref.get()
    if doc.exists:
        print(f'Document data: {doc.to_dict()}')
        doc_dict = doc.to_dict()
        #date_time = doc_dict['date_time'] # event context로 부터 작업 id 지정
        facility = doc_dict['facility']
        keywords = doc_dict['keywords']
        # 공장 정보 읽기
        doc_ref = db.collection(u'facility_db').document(facility)
        doc = doc_ref.get()
        if doc.exists:
            doc_dict = doc.to_dict()
            facility_dict = doc_dict
            facility_attribute = facility_dict['attribute']
            facility_keywords = facility_dict['item']
    else:
        print(u'No such document!')

    # 사용항 keywords 만들기. keywords+facility_attribute+facility_keywords
    input_words = (keywords+','+facility_attribute+','+facility_keywords).split(',')

    # 유사도 측정

    # input으로 받은 단어들의 평균 벡터(문장벡터)를 구하는 함수
    def makeFeatureVec(input_words):
        # 사용할 word2vec model을 불러온다.
        model = Word2Vec.load('data/final_data_word2vec_nantest.model')
        # Index2word는 모델의 사전에 있는 단어명을 담은 리스트이다.
        corpus_index2word = model.wv.index_to_key
        # input 단어들의 벡터 구하기
        input_vectors = np.array([model.wv[word] for word in input_words if word in corpus_index2word])
        # 단어벡터의 평균
        input_sen2vec =np.nanmean(input_vectors, axis=0)

        return input_sen2vec


    words_vector = makeFeatureVec(input_words)
    # words_vector.shape : (300, _)
    # 코사인 유사도가 진행되기 위해 reshape 진행
    words_vector = words_vector.reshape(1, -1)
    # words_vector.shape : (_, 300)

    # 규정, 600, 10000의 sentence_vector 불러오기
    case600_vector = np.load('data/sentence_vector_final_r1_case600.npy')
    case10000_vector = np.load('data/sentence_vector_final_r1_case10000.npy')
    GJ_vector = np.load('data/sentence_vector_final_r1_GJ.npy')


    # 각각의 sentence_vector와 코사인 유사도 실행
    cosine_sim_600 = cosine_similarity(words_vector, case600_vector)        # input으로 받은 words와 case600()과 비교
    cosine_sim_10000 = cosine_similarity(words_vector, case10000_vector)
    cosine_sim_GJ = cosine_similarity(words_vector, GJ_vector)

    ## step 1 : index와 코사인 유사도 값이 튜플로 묶인 리스트 생성
    sim600_scores = list(enumerate(cosine_sim_600[0]))
    sim10000_scores = list(enumerate(cosine_sim_10000[0]))
    simGJ_scores = list(enumerate(cosine_sim_GJ[0]))

    ## step 2 : 코사인 유사도 값(x[1])을 기준으로 리스트 정렬
    sim600_scores = sorted(sim600_scores, key=lambda x: x[1], reverse=True)
    sim10000_scores = sorted(sim10000_scores, key=lambda x: x[1], reverse=True)
    simGJ_scores = sorted(simGJ_scores, key=lambda x: x[1], reverse=True)
    # print('정렬 후 :', sim600_scores)

    ## step 3 : 정렬된 리스트에서 상위 3개만 가져온다.
    case600_top3 = sim600_scores[:3]
    case10000_top3 = sim10000_scores[:3]
    GJ_top3 = simGJ_scores[:10]
    print(case600_top3)
    # print(case10000_top3)
    # print(GJ_top3)

    ## step 4 : 졍렬된 리스트에서 idx를 사용해 문장의 id를 가져온다.
    ## 1. 상위 3개의 인덱스 받아오기
    case600_top3_idx = [idx[0] for idx in case600_top3]
    case10000_top3_idx = [idx[0] for idx in case10000_top3]
    GJ_top3_idx = [idx[0] for idx in GJ_top3]
    ## 2. 받아온 인덱스를 사용해 id 가져오기
    ## 1) case 600
    case600_id_path = 'data/case600_id.csv'
    case600_id = pd.read_csv(case600_id_path)
    case600_id_list = [x[0] for x in case600_id.iloc[case600_top3_idx].values]
    case600_id_result = ','.join(case600_id_list)
    print(case600_id.iloc[case600_top3_idx])
    ## 2) case 10000
    case10000_id_path = 'data/case10000_id.csv'
    case10000_id = pd.read_csv(case10000_id_path)
    case10000_id_list = [x[0] for x in case10000_id.iloc[case10000_top3_idx].values]
    case10000_id_result = ','.join(case10000_id_list)
    print(case10000_id.iloc[case10000_top3_idx])
    ## 3) GJ
    GJ_id_path = 'data/GJ_id.csv'
    GJ_id = pd.read_csv(GJ_id_path)
    GJ_id_list = [x[0] for x in GJ_id.iloc[GJ_top3_idx].values]
    GJ_id_result = ','.join(GJ_id_list)
    print(GJ_id.iloc[GJ_top3_idx])
#------- 문제 없음 ---------#
    ## 규정문 조회 해오기 : case600_id_list , case10000_id_list , GJ_id_list 사용
    # 규정문 사고사례 DB 읽기
    GJ_DB = pd.read_csv('data/DB_id_GJ.csv')
    case600_DB = pd.read_csv('data/DB_id_accident_case_601.csv')
    case10000_DB = pd.read_csv('data/DB_id_accident_case_10000.csv')
    #doc_title = pd.read_csv('')
    #print('csv 읽기')
    # 규정 상위 항목 정렬
    result_GJ_list = GJ_id_list
    total_GJ_list = []
    for i in result_GJ_list:
        temp = i.split('_')
        total_GJ_list.append(temp[0]+'_'+temp[1])
        for j in temp[2:]:
            total_GJ_list.append(total_GJ_list[-1]+'_'+j)

    total_GJ_list = set(total_GJ_list)
    total_GJ_list = list(total_GJ_list)
    total_GJ_list.sort()

    total_GJ_dict = {}
    for i in total_GJ_list:
        temp = i.split('_')[0]
        total_GJ_dict[temp] = []

    for i in total_GJ_list:
        temp = i.split('_')[0]
        total_GJ_dict[temp].append(i)

    for key in total_GJ_dict.keys():
        total_GJ_dict[key] = set(total_GJ_dict[key])
        total_GJ_dict[key] = list(total_GJ_dict[key])
        total_GJ_dict[key].sort()
    #print('규정 상위 항목 정렬')
    # 규정 상위 조회 및 쓰기 GJ_DB , case600_DB , case10000_DB
    ## doc_list 갱신
    doc_ref = db.collection(work_id).document(u'doc_list')
    doc_ref.set({
        u'doc_code_list': ','.join(total_GJ_dict.keys())
        })
    #print('doc_list 갱신')
    # 각 doc 에 대해 반복
    for key in total_GJ_dict.keys():
        #print('각 doc 에 대해 반복', key)
        id_list_ = total_GJ_dict[key]
        doc_ref = db.collection(work_id).document(key)
        doc_ref.set({
            u'doc_title': '취약시기 건설현장 안전작업 지침',
            u'id_list' : ','.join(id_list_)
            })
        for id_ in id_list_:
            #print('각 id 에 대해 반복', id_)
            row = GJ_DB[GJ_DB['id']==id_]
            #print(row)
            headings = id_.split('_')[-1]
            print(headings)
            text = headings + '  ' + row['sentence']
            print(text)
            ref = row['ref'].replace("<",'').replace(">",'') # <> 제거, 예)그림 1,그림 13,..
            print(ref)
            doc_ref = db.collection(work_id).document(key).collection(u'contents').document(id_)
            doc_ref.set({
                u'text': str(text.values[0]),
                u'ref' : str(ref.values[0])
                })
            print('각 id 에 대해 반복 끝', id_)
    print('## doc_list 갱신')
    # 사고사례600 조회

    # 사고사례10000 조회



    doc_ref = db.collection(u'test').document(u'zip_test')
    doc_ref.set({
  u'함수명': 'firebase 함수 테스트',
  u'work_dict': str(doc_dict),
  u'facility': facility,
  u'keywords': keywords,
  u'facility_attribute': facility_attribute,
  u'facility_keywords': facility_keywords,
  u'total_keywords': keywords+facility_attribute+facility_keywords,
  u'GJ_id_result': GJ_id_result,
  u'case600_id_result': case600_id_result,
  u'case10000_id_result': case10000_id_result,
  u'event': str(event),
  u'context' : str(context)
  })
    firebase_admin.delete_app(app)