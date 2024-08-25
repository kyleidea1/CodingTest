def solution(citations):
    citations.sort()
    n = len(citations)
    
    res = 0    
    for i in range(len(citations)):
        more_cited = n-i
        if citations[i] >= more_cited:
            res = more_cited
            break
        
    return res
            
            