def solution(s, n):
    ans = ''
    for i in s:
        if i != ' ':
            if ord('a') <= ord(i) <= ord('z'):
                ans += chr(ord(i)+n if ord(i)+n <= ord('z') else ord(i)+n-26)
            elif ord('A') <= ord(i) <= ord('Z'):
                ans += chr(ord(i)+n if ord(i)+n <= ord('Z') else ord(i)+n-26)
        else:
            ans += ' '
    return ans