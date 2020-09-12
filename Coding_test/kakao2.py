from itertools import combinations

def solution(orders, course):

    answer = []
    menu_list = set(''.join(orders))
    
    for num in course:
        com = list(map(set, combinations(menu_list, num)))
        # print(com)

        total_count = [0]*len(com)
        for order in orders:
            order_list = list(order)
            order_com = list(map(set, combinations(order_list, num)))
            # print(order_com)
            
            order_count = []
            for i in com:
                order_count.append(order_com.count(i))
            # print(order_count)
            for j in range(len(com)):
                total_count[j] += order_count[j]
        # print(total_count)
        
        if max(total_count) > 1:
            max_val = max(total_count)
            i = 0
            ind = []
            for val in total_count:
                if val == max_val:
                    ind.append(i)
                i = i + 1
        else:
            continue
        
        
        # print(ind)
        for i in ind:
            # answer.append(com[i])
            out = ''.join(sorted(com[i]))
            answer.append(out)
            
        # print(com[total_count.index(max(total_count))])

    return sorted(answer)