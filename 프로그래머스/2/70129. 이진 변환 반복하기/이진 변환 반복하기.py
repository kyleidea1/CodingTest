def solution(s):
    removed_z, cnt = 0,0
    while s != '1':
        s,z = remove_zero(s)
        removed_z += z
        cnt += 1
    return cnt,removed_z

def remove_zero(s):
    o,z = 0,0
    for l in s:
        if l == '0':
            z += 1
        else:
            o += 1
    res = bin(o)[2:]
    return res,z # 남은 1 개수, 없앤 0 개수
    
            