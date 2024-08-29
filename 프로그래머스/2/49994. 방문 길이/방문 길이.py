def solution(dirs):
    map = [[False]*10 for _ in range(10)]
    x,y = (5,5)
    loads = []
    dir = {'U':(0,1), 'R':(1,0), 'D':(0,-1), 'L':(-1,0)}
    for d in dirs:
        tmp = [(x,y)]
        if 0 <= x+dir[d][0] < 11 and 0 <= y+dir[d][1] < 11:
            x += dir[d][0]
            y += dir[d][1]
            tmp.append((x,y))
            if tmp not in loads and [tmp[1],tmp[0]] not in loads:
                loads.append(tmp)
    return len(loads)

# 다음에 풀 때 set으로 풀어보기