def solution(x, n):
    return [i for i in range(x,x+n*x,x)] if x != 0 else [x]*n