from typing import Generator, Iterable, Union


# trying to do this without itertools.chain.from_iterable()
# or itertools.chain(*iterable)
def deep_flatten(data: Iterable) -> Generator[Union[str, bytes, int], None, None]:
    for item in data:
        # bytes and str are Iterable
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from deep_flatten(item)
        else:
            yield item


if __name__ == '__main__':
    print(list(deep_flatten({(1, 2), (3, 4), (5, 6), (7, 8)})))
