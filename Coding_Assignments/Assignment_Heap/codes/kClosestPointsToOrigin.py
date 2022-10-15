from heapq import heapify, heappush
import heapq
from typing import List

points = [[3, 3], [5, -1], [-2, 4]]
k = 2


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    return heapq.nsmallest(k, points, key=lambda pair: (pair[0] ** 2 + pair[1] ** 2))


print(kClosest(points, k))
