import heapq

def solution(k, score):
    heap = []
    ans = []
    for i in range(len(score)):
        heapq.heappush(heap,score[i])
        if len(heap) > k:
            heapq.heappop(heap)
        ans.append(heap[0])
    return ans