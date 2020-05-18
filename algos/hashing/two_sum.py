'''
    Given an array of numbers and a target number, find a pair of numbers (if any) that add up to that target.
'''


# time: O(N^2)
# space: O(1)
def two_sum_slow(arr, target):
    for i in range(len(arr)): # O(N)
        for j in range(i + 1, len(arr)): # iterate through all remaining nums ~ O(N)
            if arr[i] + arr[j] == target:
                return [arr[i], arr[j]]

    return []


# time: O(2N)
# space: O(N)
def two_sum_map_fast(arr, target):
    map = {}
    for i, val in enumerate(arr): # O(N)
        map[val] = i

    for i, val in enumerate(arr): # O(N)
        if target - val in map:
            return [val, target - val]

    return []


# time: O(N)
# space: O(N)
def two_sum_map_fastest(arr, target):
    map = {}

    for i, val in enumerate(arr): # O(N)
        if target - val in map:
            return [target - val, val]
        else:
            map[val] = i

    return []


# time: O(N * log(N) + N)
# space: O(1) assuming sort in place
def two_sum_sorting(arr, target, pre_sorted=False):
    if not pre_sorted:
        arr.sort()

    left = 0
    right = len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]

        if curr_sum == target:
            return [arr[left], arr[right]]
        elif curr_sum > target:
            right -= 1
        else:
            left += 1

    return []


# time: O(N)
# space: O(1)
def two_sum_pre_sorted(arr, target):
    return two_sum_sorting(arr, target, pre_sorted=True)


def run_example():
    arr = [30, 2, 5, 11, 7]
    target = 9

    print(two_sum_slow(arr, target)) # 1
    print(two_sum_map_fastest(arr, target)) # 2
    print(two_sum_sorting(arr, target)) # 3

    sorted_arr = [2, 5, 7, 11, 30]
    target = 9

    print(two_sum_pre_sorted(sorted_arr, target)) # 4

    # respective outputs:
    '''
        1. [2, 7]
        2. [2, 7]
        3. [2, 7]
        4. [2, 7]
    '''


if __name__ == '__main__':
    run_example()
