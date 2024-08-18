def solution(s):
    s = list(s.lower())
    s[0] = s[0].upper()
    i = 1

    while i < len(s)-1:
        if s[i] == " ":
            s[i+1] = s[i+1].upper()
        i += 1
    return "".join(s)