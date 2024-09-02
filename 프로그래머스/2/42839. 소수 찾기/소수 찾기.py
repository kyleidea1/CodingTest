from itertools import permutations

def solution(numbers):
    p = []
    for i in range(1,len(numbers)+1):
        p.extend(''.join(j) for j in permutations(numbers,i))
    res = list(set(map(int,p)))
    cnt = 0
    for i in res:
        if is_prime(i):
            cnt += 1
    return cnt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True