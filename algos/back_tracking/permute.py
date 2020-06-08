def permute(arr):
    results = []
    backtrack(arr, 0, results)
    return results


def backtrack(arr, index, results):
    if index == len(arr):
        results.append(list(arr))
    else:
        for i in range(index, len(arr)):
            arr[index], arr[i] = arr[i], arr[index]
            backtrack(arr, index+1, results)
            arr[index], arr[i] = arr[i], arr[index]


def run_example():
    arr = [1, 2, 3]

    print(permute(arr)) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]


if __name__ == '__main__':
    run_example()
