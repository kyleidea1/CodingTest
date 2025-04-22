def solution(s):
    cnt = 0
    for i in s:
        if i == 'p' or i == 'P':
            cnt += 1
        elif i == 'y' or i == 'Y':
            cnt -= 1
    return True if cnt == 0 else False