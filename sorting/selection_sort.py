def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minimum = i
        for j in range(i+1, n):
            if(arr[j]<arr[minimum]):
                minimum = j
        
        temp = arr[i]
        arr[i] = arr[minimum]
        arr[minimum] = temp
    return arr

print(selection_sort([10,20,35,9,8,11,6]))