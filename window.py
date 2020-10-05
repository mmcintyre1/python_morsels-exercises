from collections import deque


class Peekable:
    sentinel = object()

    def __init__(self, iterable):
        self._iterable = iter(iterable)
        self._cache = deque()
        self._fill_cache(1)
        self._preview = self._cache[0]

    def _fill_cache(self, n=None):
        if n is None:
            n = 1
        while len(self._cache) < n+1:
            try:
                next_item = self._iterable.__next__()
            except StopIteration:
                next_item = self.sentinel
            self._cache.append(next_item)
        self._preview = self._cache[0]

    def __next__(self):
        if self._cache:
            result = self._cache.popleft()
        else:
            result = self._iterable.__next__()
        if result is self.sentinel:
            self.empty = True
            raise StopIteration
        return result

    def __iter__(self):
        return self

    def peek(self, stop=1):
        self._fill_cache(stop)
        if stop == 1:
            return [self._cache[0]]
        else:
            return [self._cache[i] for i in range(stop)]

    def is_last(self):
        return self._preview == self.sentinel


def window(iterable, n):
    if n == 0:
        return []

    p = Peekable(iterable)
    for item in p:
        lookahead = p.peek(n-1)
        if lookahead[-1] is p.sentinel:
            break
        yield tuple([item] + lookahead)


def main():
    # 1, 4, 9, 16, 25
    numbers = (n**2 for n in [1, 2, 3, 4, 5])
    it = window(numbers, 2)
    print(next(it))
    print(next(numbers))


if __name__ == '__main__':
    main()


