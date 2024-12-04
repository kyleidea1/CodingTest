def solution(arr):
    ans = 1
    for n in arr:
        gcd = get_gcd(ans,n)
        ans = ans*n//gcd 
    return ans

def get_gcd(a,b):
    while b:
        a,b = b,a%b
    return a
            