from collections import deque

def solution(n, k):
    l = [s for s in to_k_ary(n,k).split('0') if len(s) > 0]
    return len([is_prime(int(n)) for n in l if is_prime(int(n))])

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return False
    return True

def to_k_ary(n,k):
    q = deque()
    while n >= k:
        q.appendleft(str(n%k))
        n //= k
    q.appendleft(str(n%k))    
    return ''.join(q)