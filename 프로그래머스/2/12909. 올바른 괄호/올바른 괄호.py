def solution(s):
    stack = []
    for l in s:
        if l == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                return False
    return True if not stack else False