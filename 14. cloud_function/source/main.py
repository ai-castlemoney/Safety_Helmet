def hello_firestore(event, context):
    """Triggered by a change to a Firestore document.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    resource_string = context.resource
    # print out the resource string that triggered the function
    print(f"Function triggered by change to: {resource_string}.")
    # now print out the entire event object
    print(str(event))

    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import firestore

    from gensim.models import Word2Vec


    print('done')

    # 파이어베이스 앱 이니셜라이즈


    # gensim, 모델 가져오기
     


    # 작업허가서 데이터 읽어서 단어 Input 값 만들기


    # 규정 유사도 측정



    #