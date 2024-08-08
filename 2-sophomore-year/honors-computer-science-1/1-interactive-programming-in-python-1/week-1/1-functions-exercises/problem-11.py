def point_distance (x0, y0, x1, y1) :
    distance = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    return distance


def triangle_area (x0, y0, x1, y1, x2, y2) :
    point_a = point_distance(x0, y0, x1, y1)
    point_b = point_distance(x2, y2, x1, y1)
    point_c = point_distance(x0, y0, x2, y2)
    s = (point_a + point_b + point_c) / 2
    area = (s * (s - point_a) * (s - point_b) * (s - point_c)) ** 0.5
    return area