def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, p, q):
    pivot = arr[p]
    i = p
    for j in range(i + 1, q + 1):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i, p)
    return i


## Time Complexity
## Best/Average Case: O(nlogn)
## Worst Case: O(n^^2) (for almost/completly sorted array)
def quick_sort(arr, p, q):
    if p < q:
        ## Divide
        mid = partition(arr, p, q)

        ## Conquer
        quick_sort(arr, p, mid - 1)
        quick_sort(arr, mid + 1, q)

    return arr


# arr = [1, 3, 7, 9, 12, 10, 8, 16, 18, 22, 27, 0]
arr = [10, 20, 35, 9, 8]
print(quick_sort(arr, 0, len(arr) - 1))
