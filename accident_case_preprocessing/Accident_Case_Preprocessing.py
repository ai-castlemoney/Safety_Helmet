import pandas as pd
#불러올 파일의 경로를 filename 변수에 저장
data_path = 'C:/Users/김민주/project/Safety_Helmet/accident_case_preprocessing/web_scraping/test_1.csv'

#pandas read_csv로 불러오기
data = pd.read_csv(data_path)

#print(data)

#for i in range(660, 668+1):
#    content = data['sentence'][i]
#    if '재해개요' in content:
#        print('전 :', content)
#        content = content.replace('재해개요\r\n', '')  # 변수에 할당해야 적용된다. 
#        print('후 :', content)
#    
#    if '※' in content:
#        print('별 전 :', content)
#        index = content.find('※')
#        content = content[:index]
#        print('별 후 :', content)

for i in range(len(data)):
    content = data['sentence'][i]
    content = str(content)
    if ('재해개요' in content) or ('※' in content):
        content = content.replace('재해개요\r\n', '')  # 변수에 할당해야 적용된다. 
        index = content.find('※')
        content = content[:index]
        data['sentence'][i] = content

dataframe = pd.DataFrame(data)
print(dataframe)
dataframe.to_csv('C:/Users/김민주/project/Safety_Helmet/accident_case_preprocessing/web_scraping/test_preprocessing.csv', index=False)  


# import pandas as pd
# data_path = 'C:/Users/김민주/project/Safety_Helmet/accident_case_preprocessing/web_scraping/test_preprocessing.csv'
# data = pd.read_csv(data_path)
# print(data)