def boyer_moore_voting(arr):
    candidate = 0
    count = 0
    for element in arr:
        if count == 0:
            candidate = element

        count += 1 if candidate == element else -1

    frequency = 0
    for element in arr:
        if element == candidate:
            frequency += 1

    if frequency > len(arr) / 2:
        return candidate
    else:
        return -1


print(boyer_moore_voting([2, 2, 1, 1, 1, 2, 2]))
print(boyer_moore_voting([1, 2, 3]))
print(boyer_moore_voting([2, 3, 3, 7, 4]))
