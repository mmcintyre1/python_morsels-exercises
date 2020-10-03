from collections import deque


class Peekable:
    def __init__(self, iterable, cache_size=1):
        self._iterable = iter(iterable)
        self._cache = deque()
        self._cache_size = cache_size
        self._preview = self._cache[0]

    def _fill_cache(self, n):
        pass

    def peek(self, stop=1):
        if stop > len(self._cache):
            return None
        return [self._cache[i] for i in range(stop-1)]


def window(iterable, n):
    p = Peekable(iterable)
    print(list(p))
    for item in p:
        print(item)


def main():
    numbers = (n**2 for n in [1, 2, 3, 4, 5])
    print(list(window(numbers, 2)))


if __name__ == '__main__':
    main()


