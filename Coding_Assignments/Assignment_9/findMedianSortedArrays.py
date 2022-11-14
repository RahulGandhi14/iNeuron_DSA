# https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2785107/Using-Merge-Procedure

"""
Time Complexity: O(m+n)
Space Complexity: O(m+n)
"""


def findMedianSortedArraysApproach1(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    total = n1 + n2

    arr = [0] * (total)

    i = 0
    j = 0
    k = 0

    while i < n1 and j < n2:
        if nums1[i] < nums2[j]:
            arr[k] = nums1[i]
            i += 1
        else:
            arr[k] = nums2[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = nums1[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = nums2[j]
        j += 1
        k += 1

    mid = (len(arr) - 1) // 2
    if total % 2 != 0:
        return arr[mid]
    return (arr[mid] + arr[mid + 1]) / 2


"""
Time Complexity: log(min(m,n))

Intution:

Arr1 = [1,2,3,4,5,6,7,8]
Arr2 = [1,2,3,4,5]
Merged = [1,1,2,2,3,3,4,4,5,5,6,7,8]

What's median ? 
Here in our case total length of merged array is 13.
So median would be at location 6. which is 4(first occurance).

If you see carefully, median always divides array 
in two subarray of roughly same size.

Here there would be 6 items in left subarray and 6 in right subarray.

Incase of even length merged array
e.g [1,2,3,4,5,6,7,8]
Median would be average of middle two element 4 & 5 which again
divides array in two sub arrays of same size.
"""


def findMedianSortedArrays(nums1, nums2):
    total = len(nums1) + len(nums2)
    half = total // 2
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    n1 = len(nums1)
    n2 = len(nums2)

    start = 0
    end = n1 - 1

    while True:
        mid1 = start + (end - start) // 2
        # Array are 0 base indexed, that's why we're minusing 1 for mid1 and 1 for mid2
        # Thus in total we're minusing 2
        mid2 = half - mid1 - 2

        xLeft = float("-inf") if mid1 < 0 else nums1[mid1]
        xRight = float("inf") if mid1 + 1 >= n1 else nums1[mid1 + 1]
        yLeft = float("-inf") if mid2 < 0 else nums2[mid2]
        yRight = float("inf") if mid2 + 1 >= n2 else nums2[mid2 + 1]

        if xLeft <= yRight and yLeft <= xRight:
            return (max(xLeft, yLeft) + min(xRight, yRight)) / 2 if total % 2 == 0 else min(xRight, yRight)
        elif xLeft > yRight:
            end = mid1 - 1
        else:
            start = mid1 + 1


# arr1 = [23, 26, 31, 35]
# arr2 = [3, 5, 7, 9, 11, 16]
arr1 = [1, 3]
arr2 = [2]
print(findMedianSortedArraysApproach1(arr1, arr2))
print(findMedianSortedArrays(arr1, arr2))
