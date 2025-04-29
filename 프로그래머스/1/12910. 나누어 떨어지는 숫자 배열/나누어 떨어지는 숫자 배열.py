def solution(arr, divisor):
    l = [i for i in arr if i%divisor == 0]
    return sorted(l) if l else [-1]