def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0
#클래식한 이진탐색 함수

n = int(input())
array = list(map(int, input().split()))
array.sort()  # 정렬이 돼 있는 리스트에서 이진 탐색을 할 수 있다!!
m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    print(binary_search(array, target, 0, n-1))
