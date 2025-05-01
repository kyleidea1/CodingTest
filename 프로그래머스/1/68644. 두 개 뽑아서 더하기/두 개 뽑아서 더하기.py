def solution(l):
    dic = dict()
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j] not in dic:
                dic[l[i]+l[j]] = True
    return sorted(list(dic.keys()))