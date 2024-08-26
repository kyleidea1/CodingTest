from collections import deque

def solution(progresses, speeds):
    pq = deque(progresses)
    sq = deque(speeds)
    ans = []
    while pq:
        for i in range(len(pq)):
            pq[i] += sq[i]
        cnt = 0
        while pq and pq[0] >= 100:
            pq.popleft()
            sq.popleft()
            cnt += 1
        if cnt != 0:
            ans.append(cnt)
    return ans
