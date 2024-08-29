import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while any(s < K for s in scoville):
        if len(scoville) == 2 and min(scoville)+2*max(scoville) < K:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first+2*second)
        cnt += 1
    return cnt