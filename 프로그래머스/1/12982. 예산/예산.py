def solution(d, budget):
    d.sort(reverse = True)
    cnt = 0
    while d and budget >= d[-1]:
        budget -= d.pop()
        cnt += 1
    return cnt