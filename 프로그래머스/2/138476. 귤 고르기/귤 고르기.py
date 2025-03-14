def solution(k, tangerine):
    dic = dict()
    for t in tangerine:
        if t not in dic:
            dic[t] = 1
        else:
            dic[t] += 1
    dic = sorted(dic.items(), key = lambda x:x[1], reverse = True)
    summ = 0
    cnt = 0
    for i in range(len(dic)):
        if summ < k:
            summ += dic[i][1]
            cnt += 1
    return cnt
    
    
    
    
    
    
    
    
    
   














    # dic = dict()
    # for t in tangerine:
    #     if t not in dic:
    #         dic[t] = 1
    #     else:
    #         dic[t] += 1
    # desc = sorted(dic.values(), reverse = True)
    # sum = 0
    # for i in range(len(desc)):
    #     sum += desc[i]
    #     if sum >= k:
    #         break
    # return i+1