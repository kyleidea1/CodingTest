def solution(nums):
    n = len(set(nums))
    return n if n <= len(nums)//2 else len(nums)//2