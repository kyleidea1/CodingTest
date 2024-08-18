def solution(s):
    temp = [s[0]]
    for i in range(1,len(s)):
        if temp:
            if s[i] != temp[-1]:
                temp.append(s[i])
            else:
                temp.pop()
        else:
            temp.append(s[i])
    return 1 if not temp else 0
        
