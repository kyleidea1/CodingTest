def solution(number, limit, power):
    l = [count_div(i) for i in range(1,number+1)]
    return sum([i if i <= limit else power for i in l])

def count_div(n):
    if n == 1:
        return 1
    else:
        cnt = 2
        for i in range(2,int(n**(1/2)+1)):
            if n % i == 0:
                if n // i == i:
                    cnt += 1
                else:
                    cnt += 2
    return cnt