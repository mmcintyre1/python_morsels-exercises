class OrderedSet:
    def __init__(self, items):
        # with python 3.7, dicts are guaranteed to maintain insertion order
        self.items = {k: None for k in items}

    def __iter__(self):
        yield from self.items

    def __contains__(self, key):
        return key in self.items

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        if not isinstance(other, OrderedSet):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.foo == other.foo and self.bar == other.bar

    def add(self, value):
        self.items[value] = None

    def discard(self, value):
        try:
            del self.items[value]
        except KeyError:
            pass


if __name__ == '__main__':
    print(*OrderedSet("Hello world.  This string contains many characters in it."))
