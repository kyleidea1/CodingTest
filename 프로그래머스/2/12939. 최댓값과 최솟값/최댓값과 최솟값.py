def solution(s):
    l = list(map(int, s.split()))
    return "{0} {1}".format(min(l),max(l))