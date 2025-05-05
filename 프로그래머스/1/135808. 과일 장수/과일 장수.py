def solution(k, m, score):
    score.sort(reverse = True)
    split_score = [score[i:i+m] for i in range(0,len(score),m)]
    ans = 0
    for s in split_score:
        if len(s) == m:
            ans += min(s)*m
    return ans