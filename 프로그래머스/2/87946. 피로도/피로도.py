from itertools import permutations

def solution(k, dungeons):
    l = []
    permutation = permutations(dungeons, len(dungeons))
    for p in permutation:
        l.append(process(p,k))
    return max(l)

def process(p,k):
    cnt = 0
    for i in p:
        if k >= i[0]:
            k -= i[1]
            cnt += 1
    return cnt