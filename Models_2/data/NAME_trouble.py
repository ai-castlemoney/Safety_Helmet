import re
import pandas as pd
from konlpy.tag import Mecab

data_path = "Models/final_data.csv"
data = pd.read_csv(data_path)
text = data['sentence'][11308]
print(text)
corpuses = re.sub(r'[^ ㄱ-ㅣ가-힣A-Za-z]', '', text)  # 특수기호, 한자 제거
print(corpuses)

mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")
token = mecab.nouns(corpuses)
print(token)    # 빈 문자 리스트가 반환된다. (외국어(영어)는 품사가 SL)

# 출력결과
# #NAME?, #NAME?
# NAME NAME
# []
