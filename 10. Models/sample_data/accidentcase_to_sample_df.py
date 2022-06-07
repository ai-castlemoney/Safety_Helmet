import pandas as pd

data_path = 'C:/Users/김민주/project/Safety_Helmet/TF_IDF_test/sample_data/final_case_utf8.csv'

data = pd.read_csv(data_path)
#print(data.head(5))
#print('Before delect :', data.columns)

want_to_del = ['Unnamed: 0', '사고명', '발생일시', '사고인지 시간', '공공/민간 구분', '기상상태', '시설물 종류',
       '인적사고', '보호(방호)조치여부', '물적사고', '공종', '사고객체', '작업프로세스', '장소', '부위',
       '사고원인', '사망자수(명)', '부상자수(명)', '피해금액', '피해내용', '사고신고사유', '사고발생후 조치사항', 
       '재발방지대책', '공사종류', '공사비', '낙찰률', '공사기간', '공정률', '작업자수', '안전관리계획', '설계안전성검토', 
       '사고조사방법', '위원회조사필요성', '위원회구성(안)', '향후조치계획']

data_del = data.drop(columns=want_to_del, axis=1)
#print('After delect :', data_del.columns)
#print(data_del)

#print('사고경위 길이 :', len(data_del['사고경위']))
#print('구체적 사고원인 :', len(data_del['구체적 사고원인']))

#data_del['sentence'] = data_del['사고경위'].copy
#for i in range(len(data_del['구체적 사고원인'])):
#    data_del['sentence'].append(data_del['구체적 사고원인'][i])

total_data = []
for i in range(len(data_del['사고경위'])):
    total_data.append(data_del['사고경위'][i])
for i in range(len(data_del['구체적 사고원인'])):
    total_data.append(data_del['구체적 사고원인'][i])

#print('전체 길이 :', len(total_data))

list_df = pd.DataFrame(total_data, columns=['sentence'])
#print(list_df.head())
#print(list_df.tail())
list_df.to_csv('C:/Users/김민주/project/Safety_Helmet/TF_IDF_test/sample_data/accident_train_sample.csv')
