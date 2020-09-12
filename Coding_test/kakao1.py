def solution(new_id):
    ans_list = []
    for i in range(len(new_id)):
        if new_id[i] in ['~','!','@','#','$','%','^','&','*','(',')','=','+','[','{',']','}',':','?',',','<','>']:
            i += 1
        else:
            ans_list.append(new_id[i].lower())
            
    i = 0
    while i != len(ans_list) - 1:
        if ans_list[i] == '.' and ans_list[i+1] == '.':
            ans_list.pop(i)
        else:
            i += 1
            
    if ans_list[0] == '.':
        ans_list.pop(0)
        
    if ans_list != [] and ans_list[-1] == '.':
        ans_list.pop()
        
    if ans_list == []:
        ans_list.append('a')
        
    if len(ans_list) >= 16:
        ans_list = ans_list[:15]
        if ans_list[-1] == '.':
            ans_list.pop(-1)
            
    if len(ans_list) <= 2:
        while len(ans_list) < 3:
            ans_list.append(ans_list[-1])
        
    answer = ''.join(ans_list)
    return answer