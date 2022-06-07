# import csv

# # 사고사례 600의 id를 리스트로 만들기
# case600_id_list = []
# f = open("Models_2/data/case600_id.csv",'r')
# rea = csv.reader(f)
# for row in rea:
#     case600_id_list.append(row)
# f.close
# print(case600_id_list[:3])

# # 사고사례 10000의 id를 리스트로 만들기
# case10000_id_list = []
# f = open("Models_2/data/case10000_id.csv",'r')
# rea = csv.reader(f)
# for row in rea:
#     case10000_id_list.append(row)
# f.close
# print(case10000_id_list[:3])

# # 규정의 id를 리스트로 만들기
# GJ_id_list = []
# f = open("Models_2/data/GJ_id.csv",'r',encoding='utf-8-sig')
# rea = csv.reader(f)
# for row in rea:
#     GJ_id_list.append(row)
# f.close
# print(GJ_id_list[:3])

def csv2list(filename):
    import csv
    file = open('Models_2/data/'+filename, 'r', encoding='utf-8-sig')
    csvfile = csv.reader(file)
    lists = []
    for item in csvfile:
        data = ', '.join(item)
        lists.append(data)
    return lists

print(csv2list("case600_id.csv")[:3])
print(csv2list("case10000_id.csv")[:3])
print(csv2list("GJ_id.csv")[:3])