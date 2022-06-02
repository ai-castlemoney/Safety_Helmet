# 생성된 문장 벡터 내의 nan유무를 확인한다.

import numpy as np

# 만들어진 벡터를 불러온다.
case600_vectors = np.load('Models_2\create_sentence_vector\sentence_vector_final_r1_case600.npy')
case10000_vectors = np.load('Models_2\create_sentence_vector\sentence_vector_final_r1_case10000.npy')
GJ_vectors = np.load('Models_2\create_sentence_vector\sentence_vector_final_r1_GJ.npy')

# print(type(case600_vectors))

# 넘파이 배열 안에 nan이 있는지 확인해본다. 
# array_sum_600 = np.sum(case600_vectors)
# check = np.isnan(array_sum_600)
# print('600 :', check)

# array_sum_10000 = np.sum(case10000_vectors)
# check = np.isnan(array_sum_10000)
# print('10000 :', check)

# array_sum_GJ = np.sum(GJ_vectors)
# check = np.isnan(array_sum_GJ)
# print('GJ :', check)

