import re
import pandas as pd

data_path = "Models/final_data.csv"
data = pd.read_csv(data_path)
text = data['sentence'][11308]
print(text)
corpuses = re.sub(r'[^ ㄱ-ㅣ가-힣A-Za-z]', '', text)  # 특수기호, 한자 제거
print(corpuses)