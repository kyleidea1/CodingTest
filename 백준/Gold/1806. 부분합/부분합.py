def min_subarray_length_two_pointers(N, S, array):
    min_length = N + 1
    current_sum = 0
    start = 0

    for end in range(N):
        current_sum += array[end]
        while current_sum >= S:
            min_length = min(min_length, end - start + 1)
            current_sum -= array[start]
            start += 1

    return min_length if min_length <= N else 0

N, S = map(int, input().split())
array = list(map(int, input().split()))

print(min_subarray_length_two_pointers(N, S, array))