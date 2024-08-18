def solution(s):
    cnt, zero = 0, 0
    while s != '1':
        s, removed_zero = conversion(s)
        cnt += 1
        zero += removed_zero
    return [cnt,zero]

def conversion(s):
    one = s.count('1')
    removed_zero = len(s) - one
    one_bin = bin(one)[2:]
    return one_bin, removed_zero
    