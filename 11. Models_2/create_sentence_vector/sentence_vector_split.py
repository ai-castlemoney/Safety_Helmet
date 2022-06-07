# 하나로 합쳐져 있는 sentence_vector를 각각 규정, 사고사례 600, 10000으로 나누기

import numpy as np

# 저장되어 있는 넘파이 배열 불러오기
sentence_vector = np.load('C:/Users/김민주/project/Safety_Helmet/Models_2/create_sentence_vector/final_data_r1_sentence_vector_nanmean.npy')

# 규정 길이 : 7593
# 사고사례 600 길이 : 602
# 사고사례 10000 길이 : 11919

# 넘파이 shape : (20114, 300)
print(sentence_vector.shape)
#print(sentence_vector.dtype)

vector_GJ = sentence_vector[:7592+1]
print(vector_GJ.shape)
vector_case600 = sentence_vector[7593:8194+1]
print(vector_case600.shape)
vector_case10000 = sentence_vector[8195:]
print(vector_case10000.shape)


np.save('C:/Users/김민주/project/Safety_Helmet/Models_2/create_sentence_vector/sentence_vector_final_r1_case600.npy', vector_case600)
np.save('C:/Users/김민주/project/Safety_Helmet/Models_2/create_sentence_vector/sentence_vector_final_r1_case10000.npy', vector_case10000)
np.save('C:/Users/김민주/project/Safety_Helmet/Models_2/create_sentence_vector/sentence_vector_final_r1_GJ.npy', vector_GJ)
print('done :)')