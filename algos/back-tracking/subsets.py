def subsets(arr):
    results = []
    backtrack(0, [], arr, results)
    return results


def backtrack(index, curr, arr, results):
    if index == len(arr):
        results.append(list(curr)) # dump running subset
        return

    # explore including current val at index
    curr.append(arr[index])
    backtrack(index + 1, curr, arr, results)

    # remove what we last added to backtrack
    curr.pop()
    backtrack(index + 1, curr, arr, results)


def run_example():
    arr = [1, 2, 3]

    print(subsets(arr)) # [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]


if __name__ == '__main__':
    run_example()