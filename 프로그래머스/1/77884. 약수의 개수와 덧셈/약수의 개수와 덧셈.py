def find_div_num(n):
    if n == 1:
        return 1
    else:
        cnt = 2
        i = 2
        while i < n//2+1:
            if n % i == 0:
                cnt += 1
            i += 1
    return cnt

def solution(left, right):
    sum = 0
    for i in range(left,right+1):
        sum += (i if find_div_num(i)%2==0 else -i)
    return sum