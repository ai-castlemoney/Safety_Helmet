import pandas as pd

path = '/Users/namcheolher/aiffel/Safety_Helmet/cloud_function/cloud_function_zip/data/title.csv'

doc_title_DB = pd.read_csv(path)

print(doc_title_DB)