from collections import Counter

def solution(clothes):
    dic = dict()
    for c in clothes:
        if c[1] not in dic.keys():
            dic[c[1]] = 0
        dic[c[1]] += 1
    
    ans = 1
    ds = [d for d in dic.values()]
    for i in range(len(ds)):
        ans *= (ds[i]+1)
        
    return ans-1