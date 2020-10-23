import itertools


def interleave(*args):
    sentinel = object()
    for items in itertools.zip_longest(*args, fillvalue=sentinel):
        for item in items:
            if item is not sentinel:
                yield item


def main():
    in1 = [1, 2, 3]
    squares = (n ** 2 for n in in1)
    output = interleave(squares, squares)
    print(next(output))
    print(next(output))
    print(next(squares))


if __name__ == '__main__':
    main()
