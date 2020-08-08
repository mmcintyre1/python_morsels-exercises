def add(*args):
    """
    Adds nested matrices together and outputs
    in the same format as given, as in, if the following matrices,
    matrix 1 [[1,2], [3,4]] and matrix 2 [[5,6], [7,8]] are added
    together, the result is [[6,8], [10,12]].

    Throws a ValueError if the matrices are not the same shape
    """
    if any(len(error_value := group) != len(args[0]) for group in args):
        raise ValueError(f"Given matrices {error_value} are not the same size.")

    res = []
    for x in zip(*args):
        if any(len(error_value := group) != len(x[0]) for group in x):
            raise ValueError(f"Given matrices {error_value} are not the same size.")
        res.append([sum(y) for y in zip(*x)])

    return res


if __name__ == '__main__':
    m1 = [[6, 6], [3, 1]]
    m2 = [[1, 2], [3, 4], [5, 6]]
    r = add(m1, m2)
    print(r)
