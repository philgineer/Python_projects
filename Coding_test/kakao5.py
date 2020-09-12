def to_second(time):
    return sum(x * int(t) for x, t in zip([3600, 60, 1], time.split(":"))) 

def solution(play_time, adv_time, logs):
    
    play_time_s = to_second(play_time)
    adv_time_s = to_second(adv_time)
    
    time_vector = [0] * play_time_s

    data = []
    
    for i in logs:
        start, end = map(to_second, i.split('-'))
        for j in range(end-start):
            time_vector[start + j] += 1
            
    sum_list = []
    for i in range(play_time_s):
        sum_list.append(sum(time_vector[i:i+adv_time_s]))
        
    seconds = sum_list.index(max(sum_list))
    
    if len(str(seconds // 3600)) == 1:
        two_letter = '0' + str(seconds // 3600)
    else:
        two_letter = str(seconds // 3600)
    
    answer = two_letter + ':' + str((seconds%3600) // 60) + ':' + str((seconds%3600) % 60)
    return answer