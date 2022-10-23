def collinearPoints(points):
    p1, p2, p3 = points

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    if (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2):
        return "Yes"
    else:
        return "No"


def usingAreaOfTriangle(points):
    p1, p2, p3 = points

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    area = 0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    if area == 0:
        return "Yes"
    else:
        return "No"


print("Approach 1", collinearPoints([(1, 1), (1, 4), (1, 5)]))
print("Approach 2", usingAreaOfTriangle([(1, 1), (1, 4), (1, 5)]))
print("Approach 1", collinearPoints([(1, 1), (1, 6), (0, 9)]))
print("Approach 2", usingAreaOfTriangle([(1, 1), (1, 6), (0, 9)]))
