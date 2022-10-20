def collinearPoints(points):
    p1, p2, p3 = points

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    if (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2):
        return "Yes"
    else:
        return "No"


print(collinearPoints([(1, 1), (1, 4), (1, 5)]))
print(collinearPoints([(1, 1), (1, 6), (0, 9)]))
