import numpy as np

score_list = np.random.randint(0, 10, size=(1000))
#print(score_list)

''' list '''
M, m = None, None
for score in score_list:
    if M == None or score > M:
        M = score
    if m == None or score < m:
        m = score
        
print("M - m: ", M - m)

cnt_list = [0 for i in range(M - m)]
print(cnt_list, len(cnt_list))

for score in score_list:
    cnt_list[score - 1] = cnt_list[score - 1] + 1
print("cnt_list: ", cnt_list)

''' dict '''
tmp_dict = dict()
tmp_dict['A'] = 10
tmp_dict['B'] = 20
tmp_dict['F'] = 100
print("tmp_dict: ", tmp_dict)

cnt_dict = dict()
for score in score_list:
    cnt_dict[score] = cnt_dict.get(score, 0) + 1

print("cnt_dict ", cnt_dict)
print("5/9점 맞은 인원수: ", cnt_dict[5])

key_list = list(cnt_dict.keys())
val_list = list(cnt_dict.values())
item_list = cnt_dict.items()

for key, val in cnt_dict.items():
    print("key: ", key, ", val: ", val)