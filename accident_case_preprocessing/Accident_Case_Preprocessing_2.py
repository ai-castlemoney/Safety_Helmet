import pandas as pd
#불러올 파일의 경로를 filename 변수에 저장
data_path = 'accident_case_preprocessing/test_1.csv'

#pandas read_csv로 불러오기
data = pd.read_csv(data_path)

# print(data)

for i in range(len(data)):
    content = data['sentence'][i]
    content = str(content)
    if ('재해개요' in content) or ('※' in content):
        content = content.replace('재해개요\r\n', '')  # 변수에 할당해야 적용된다. 
        content = content.replace("\n", "")
        index = content.find('※')
        content = content[:index]
        data['sentence'][i] = content

dataframe = pd.DataFrame(data)

print(dataframe)
dataframe.to_csv('accident_case_preprocessing/test_preprocessing2.csv', index=False, encoding='utf-8')
print('done')  