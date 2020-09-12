# def remove_all(elements, list):
#     return filter(lambda x: x not in elements, list)

def solution(info, query):
    
    info_data = []
    query_data = []
    
    answer = []
    
    for i in range(len(info)):
        # print(info[i].split())
        info_data.append(info[i].split())
        # info_data[i][-1] = int(info_data[i][-1])
        
    for i in range(len(query)):
        # print(list(remove_all('and', query[i].split())))
        # query_data.append(list(remove_all('and', query[i].split())))   
        query_data.append(query[i].split())
    
    for i in query_data:
        count = 0
        for j in info_data:
            correct = []
            for k in range(4):
                if int(j[-1]) < int(i[-1]) or i[2*k] not in [j[k], '-']:
                        pass
                else:
                    correct.append(True)
            if correct == [True, True, True, True]:
                count += 1
        answer.append(count)
    
    return answer