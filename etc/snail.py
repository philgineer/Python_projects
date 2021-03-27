n = 5

# init map
map = [[0 for _ in range(n)] for _ in range(n)]

# print init
print("### Init ###")
for i in range(n):
    print(map[i])

# snale
flag = ['right', 'down', 'left', 'up']
flag_idx = 0
i, j = 0,0

def change_flag():
    global i, j, map, flag_idx
    if i < 0 or i >= n or j < 0 or j >= n or map[j][i] != 0:
        flag_idx += 1
        flag_idx = flag_idx % 4
        return True
    return False

for num in range(1, n ** 2 + 1):
    map[j][i] = num

    if flag[flag_idx] == 'right':
        i += 1
        if change_flag():
            i -= 1
    if flag[flag_idx] == 'down':
        j += 1
        if change_flag():
            j -= 1
    if flag[flag_idx] == 'left':
        i -= 1
        if change_flag():
            i += 1
    if flag[flag_idx] == 'up':
        j -= 1
        if change_flag():
            j += 1
            i += 1

    # Debug
    print('map[{}][{}] = {}, flag_idx={}, flag={}'.format(j, i, num, flag_idx, flag[flag_idx]))
    for k in range(n):
        print(map[k])
        print()


# print snale
print("### Snale ###")
for i in range(n):
    print(map[i])
