def solution(n):
    answer = []
    i = 1
    while i <= (n+1)//2:
        if n % i == 0:
            answer.append(i)
        i += 1
    return sum(answer)+n if n != 1 else 1