def solution(p, limit):
    p.sort()
    l = 0
    r = len(p)-1
    boats = 0
    
    while l <= r:
        if p[l]+p[r] <= limit:
            l += 1
        r -= 1
        boats += 1
            
    return boats