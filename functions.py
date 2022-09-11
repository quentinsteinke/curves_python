# Linear interpolation -- Formula - p1 * (1 - t) + p2 * t
def lerp(p1, p2, t):
    p1 = [(1 - t) * i for i in p1]
    p2 = [t * i for i in p2]

    position = [p1[0] + p2[0], p1[1] + p2[1]]

    return position


def tupleSub(tuple1, tuple2):
    tuple3 = []
    if len(tuple1) == len(tuple2):
        for i, x in enumerate(tuple1):
            z = x - tuple2[i]
            tuple3.append(z)
    
    return tuple3

