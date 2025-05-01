def solution(food):
    l = [i//2 for i in food]
    ans = ''
    for i in range(1,len(l)):
        ans += l[i]*str(i)
    tmp = ans[::-1]
    ans += '0'
    ans += tmp
    return ans