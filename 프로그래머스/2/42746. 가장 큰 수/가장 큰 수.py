from functools import cmp_to_key

def compare(a,b):
    return -1 if a+b > b+a else 1

def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key = cmp_to_key(compare))
    return ''.join(numbers) if numbers[0] != '0' else '0'