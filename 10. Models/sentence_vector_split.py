# 하나로 합쳐져 있는 sentence_vector를 각각 사고사례 600, 10000, 규정으로 나누기

import numpy as np

# 저장되어 있는 넘파이 배열 불러오기
sentence_vector = np.load('C:/Users/김민주/project/Safety_Helmet/Models/sentence_vector/final_data_sentence_vector.npy')

# 사고사례 600 길이 : 602
# 사고사례 10000 길이 : 11921
# 규정 길이 : 7593
# 넘파이 shape : (20116, 300)
print(sentence_vector.shape)
print(sentence_vector.dtype)

vector_case600 = sentence_vector[:601+1]
#print(vector_case600.shape)
#print(type(vector_case600))
vector_case10000 = sentence_vector[602:12522+1]



print(vector_case10000.shape)
vector_GJ = sentence_vector[12523:]
print(vector_GJ.shape)
array_sum = np.sum(vector_case600)
array_has_nan = np.isnan(array_sum)

print(array_has_nan, '?')
# np.save('C:/Users/김민주/project/Safety_Helmet/Models/sentence_vector/sentence_vector_final_case600.npy', vector_case600)
# np.save('C:/Users/김민주/project/Safety_Helmet/Models/sentence_vector/sentence_vector_final_case10000.npy', vector_case10000)
# np.save('C:/Users/김민주/project/Safety_Helmet/Models/sentence_vector/sentence_vector_final_GJ.npy', vector_GJ)
# print('done :)')