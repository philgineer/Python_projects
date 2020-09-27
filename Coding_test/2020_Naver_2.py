def solution(blocks):
    length = 0
    level = []
    
    for i in range(len(blocks)+1):
        level.append(length + i)
        length += i
        
    INF = 10e9
    result = [INF] * length
    
    for i in range(len(blocks)):
        result[level[i] + blocks[i][0]] = blocks[i][1]
        
    table = []
    for i in range(len(level)-1):
        table.append(result[level[i]:level[i+1]])
        
    for i in range(1, len(table)):
        while INF in table[i]:
            for j in range(len(table[i])):
                if table[i][j] != INF and j==0:
                    table[i][j+1] = table[i-1][j] - table[i][j]
                elif table[i][j] != INF:
                    table[i][j-1] = table[i-1][j-1] - table[i][j]
                if table[i][j] != INF and j < len(table[i]) - 1:
                    table[i][j+1] = table[i-1][j] - table[i][j]
                    
    answer = []
    for i in table:
        for j in i:
            answer.append(j)
    return answer