def solution(m, k):
    m_list = list(m)
    answer = ''
    for i in k:
        answer += m[:m.index(i)]
        m = m[m.index(i)+1:]
    return answer+m