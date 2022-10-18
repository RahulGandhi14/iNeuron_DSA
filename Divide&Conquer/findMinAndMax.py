def findMinAndMax(arr, i, j):
    if i == j:
        min_val = arr[i]
        max_val = arr[j]
    elif i == j - 1:
        if arr[i] < arr[j]:
            min_val = arr[i]
            max_val = arr[j]
        else:
            min_val = arr[j]
            max_val = arr[i]
    else:
        # Divide And Conquer
        mid = i + (j - i) // 2
        min1, max1 = findMinAndMax(arr, i, mid)
        min2, max2 = findMinAndMax(arr, mid + 1, j)

        if min1 < min2:
            min_val = min1
        else:
            min_val = min2

        if max1 > max2:
            max_val = max1
        else:
            max_val = max2

    return (min_val, max_val)


arr = [10, 15, 5, 20, 25, 31, 27, 29]
print(findMinAndMax(arr, 0, len(arr) - 1))
