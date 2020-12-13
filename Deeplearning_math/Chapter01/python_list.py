tmp_list = [(i+10) for i in range(100)]

for data_idx in range(len(tmp_list)):
    if 50 <= data_idx <= 59:
        print(data_idx - 49, ": ", tmp_list[data_idx])

sum_val = 0
data_cnt = 0
for data_idx, data in enumerate(tmp_list):
    if data_idx >= 50 and data_idx < 60:
        sum_val += data
        data_cnt += 1
mean = sum_val / data_cnt
print("Mean: ", mean)

M, m = None, None
for data in tmp_list[50:60]:
    if M == None or data > M:
        M = data
    if m == None or data < m:
        m = data
print("Max: ", M, " Min: ", m)

score_list = [(2*i+10) for i in range(45)] + [-1]
grade_list = [0, 0, 0]
for score in score_list:
    if score >= 90 and score < 100:
        grade_list[0] += 1
    elif score >= 80 and score <90:
        grade_list[1] += 1
    elif score >= 0 and score < 80:
        grade_list[2] += 1
    else:
        class ScoreError(Exception):
            pass
        raise ScoreError("Invalid Score")

print(grade_list)
        