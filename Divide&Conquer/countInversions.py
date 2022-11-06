# https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1


def count_inversions_combine(arr, left, mid, right, count):
    ## length of first sub array
    n1 = mid - left + 1

    ## length of second sub array
    n2 = right - mid

    ## initialization of left and right sub array
    leftSubArr = [0] * n1
    rightSubArr = [0] * n2

    ## copy the elements from an array to sub arrays
    ## left sub array
    for i in range(n1):
        leftSubArr[i] = arr[left + i]
    ## right sub array
    for i in range(n2):
        rightSubArr[i] = arr[mid + 1 + i]

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if leftSubArr[i] > rightSubArr[j]:
            arr[k] = rightSubArr[j]
            j += 1
            """
            Explanation: Suppose left arr is [3,5,6] and right arr is [2].
            Now for i and j is equal 0, arr[i] > arr[j], i.e 3>2,
            thus all rest of the elements at index k>i in left subarray
            would be greater then the element at jth location of right subarray.
            thus adding (n1 - (i+1)) in count.
            """
            count += 1 + n1 - (i + 1)
        else:
            arr[k] = leftSubArr[i]
            i += 1
        k += 1

    ## Copy remaining elements for left sub array
    while i < n1:
        arr[k] = leftSubArr[i]
        i += 1
        k += 1

    ## Copy remaining elements for right sub array
    while j < n2:
        arr[k] = rightSubArr[j]
        j += 1
        k += 1

    return count


def count_inversions(arr, left, right, count):
    if left < right:
        mid = left + (right - left) // 2
        count1 = count_inversions(arr, left, mid, 0)
        count2 = count_inversions(arr, mid + 1, right, 0)
        count = count_inversions_combine(arr, left, mid, right, count1 + count2)

    return count


arr = [6, 3, 5, 2, 7]
print("Inversions:", count_inversions(arr, 0, len(arr) - 1, 0))

arr = [2, 3, 4, 5, 6]
print("Inversions:", count_inversions(arr, 0, len(arr) - 1, 0))
