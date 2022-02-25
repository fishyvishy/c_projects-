from typing import List, Tuple


def linear(points: List[Tuple[float]], t: float, animate: bool) -> List[Tuple[float]]:
    assert len(points) == 2
    p0, p1 = points[0], points[1]
    x = p0[0] + t * (p1[0] - p0[0])
    y = p0[1] + t * (p1[1] - p0[1])
    if animate:
        return tuple([x, y])
    return [tuple([x, y])]


def quadratic(points: List[Tuple[float]], t: float, animate: bool) -> List[Tuple[float]]:
    assert len(points) == 3
    p0, p1, p2 = points[0], points[1], points[2]
    x = ((1 - t)**2)*p0[0] + 2*(1 - t)*t* p1[0] + (t**2)* p2[0]
    y = ((1 - t)**2)*p0[1] + 2*(1 - t)*t* p1[1] + (t**2)* p2[1]
    if animate:
        q0, q1 = linear([p0, p1], t, True), linear([p1, p2], t, True)
        return [(x, y), [q0, q1]]
    return [tuple([x, y])]


def cubic(points: List[Tuple[float]], t: float, animate: bool) -> List[List[Tuple[float]]]:
    assert len(points) == 4
    p0, p1, p2, p3 = points[0], points[1], points[2], points[3]
    x = ((1 - t)**3)*p0[0] + 3*((1 - t)**2)*t*p1[0] + 3*(1 - t)*(t**2)*p2[0] + (t**3)*p3[0]
    y = ((1 - t)**3)*p0[1] + 3*((1 - t)**2)*t*p1[1] + 3*(1 - t)*(t**2)*p2[1] + (t**3)*p3[1]
    if animate:
        z0, z1, z2 = linear([p0, p1], t, True), linear([p1, p2], t, True), linear([p2, p3], t, True)
        t0, t1 = linear([z0, z1], t, True), linear([z1, z2], t, True)
        return [tuple([x, y]), [z0, z1, z2], [t0, t1]]
    return [tuple([x, y])]

