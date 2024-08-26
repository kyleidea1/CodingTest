from collections import deque

def solution(priorities, location):
    index = [i for i in range(len(priorities))]
    dic = dict(zip(index, priorities))
    q = deque(dic.items())
    cnt = 1
    
    while q:
        item = q.popleft()
        if any(i[1] > item[1] for i in q):
            q.append(item)
        else:
            if item[0] == location:
                return cnt
            else:
                cnt += 1