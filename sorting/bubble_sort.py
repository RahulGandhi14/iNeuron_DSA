def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[i]>arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


print(bubble_sort([10,20,35,9,8,11,6,36]))