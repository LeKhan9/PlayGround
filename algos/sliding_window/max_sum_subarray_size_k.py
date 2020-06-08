def max_sum_subarray_size_k(arr, k, return_sub_array=False):
    ''' Given an array of positive integers, return the max sum from any sub-array in this array of size k
        Optionally, if a flag is passed to return the actual sub_array, then that will be returned

        Note: it's granted that the flag is not best design as this function is doing too many things, but this is just
        for demonstration purposes and to reduce code copy pasting to another function

        This function demonstrates the advantage of the sliding window algorithm approach instead of recalculating a
        sum of k items for each item in the array — O(N * K). By "caching" the previous sum, we can shrink and expand
        the window by one each time, hence reducing the algorithm to upperbound to O(N).
    '''

    max_sum = curr_sum = left = 0

    if return_sub_array:
        max_subarray = []

    for right in range(len(arr)):
        curr_sum += arr[right]

        # supposing we've gone through at least k items
        if right >= k - 1:
            if curr_sum > max_sum:
                max_sum = curr_sum # update max

                if return_sub_array:
                    max_subarray = arr[left: right + 1]

            # update curr_sum to shrink it so that next item can
            # become a candidate in the k sized window
            curr_sum -= arr[left]
            left += 1

    if return_sub_array:
        return max_subarray

    return max_sum


def run_example():
    arr = [2, 1, 5, 1, 3, 2]
    k = 3

    print(max_sum_subarray_size_k(arr, k))

    # prints actual max sub-array
    print(max_sum_subarray_size_k(arr, k, return_sub_array=True))



if __name__ == '__main__':
    run_example()
