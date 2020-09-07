from collections.abc import MutableSet
from itertools import zip_longest


class OrderedSet(MutableSet):
    def __init__(self, items):
        # with python 3.7, dicts are guaranteed to maintain insertion order
        self.items = dict.fromkeys(items, None)
        super().__init__()

    def __len__(self):
        return len(self.items)

    def __contains__(self, value):
        return value in self.items

    def __iter__(self):
        # this can also be written as iter(self.items.keys())
        # is there any difference?
        yield from self.items

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            # handling for exact order
            return (self is other) or all(x == y for x, y in zip_longest(self, other))
        elif isinstance(other, set):
            return set(self) == other
        return False

    # another way to write this __eq__ is below:
    # its probably cleaner, and I like the type()
    # check as opposed to an explicit check against OrderedSet
    # def __eq__(self, other):
    #     if isinstance(other, type(self)):
    #         return (
    #             len(self) == len(other) and
    #             all(x == y for x, y in zip(self, other))
    #         )
    #     return super().__eq__(other)

    def __getitem__(self, index):
        # this has to be turned into a list every index call
        # we might be able to store this into a variable? use a sentinel
        # on the add/discard methods to see if things have changed and turn
        # into a list again?
        return list(self.items.keys())[index]

    def __str__(self):
        return ", ".join(self.items.keys())

    def add(self, value):
        self.items[value] = None

    def discard(self, value):
        self.items.pop(value, None)


if __name__ == '__main__':
    words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
    print(words[1])
