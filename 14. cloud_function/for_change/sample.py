import pandas as pd

# words_path = '/Users/namcheolher/aiffel/Safety_Helmet/cloud_function/cloud_function_zip/words.tsv'
# words = pd.read_csv(words_path, sep= '\t')

# print(words['0'].values.tolist())



# python sample.py > test1.txt
# python sample.py > test1.txt
# python sample.py > test1.txt
# python sample.py > test1.txt


# 단어 벡터
words_vectors_path = '/Users/namcheolher/aiffel/Safety_Helmet/cloud_function/for_change/final_nantest_data_vectors_tsv.tsv'
words_vectors = pd.read_csv(words_vectors_path, sep='\t')
#print(words_vectors)
#print(len(words_vectors))
print(words_vectors.values.tolist())
# print(len(words_vectors.values.tolist()))
# print(len(words_vectors.values.tolist()[0]))
