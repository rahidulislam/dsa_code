def max_sum_subarray(arr, k):
    if k > len(arr):
        return None
    max_sum = 0
    window_sum = sum(arr[:k])
    # for i in range(k):
    #     window_sum += arr[i]
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum

print(max_sum_subarray([2, 3, 4, 1, 5], 2)) # 7
print(max_sum_subarray([1,12,-5,-6,50,3], 4)) # 61