import unicodedata


def NFD(text):
    return unicodedata.normalize('NFD', text)


def canonical_caseless(text):
    return NFD(NFD(text).casefold())


class FuzzyString(str):
    def __new__(cls, value):
        return super(FuzzyString, cls).__new__(cls, value)

    def __eq__(self, other):
        return canonical_caseless(self) == canonical_caseless(other)

    def __ne__(self, other):
        # in the documentation, it says "By default, __ne__() delegates to __eq__() and
        # inverts the result unless it is NotImplemented." but that doesn't seem to work
        return not self.__eq__(other)

    def __lt__(self, other):
        return [ord(c) for c in self] > [ord(c) for c in other]

    def __gt__(self, other):
        return not self.__lt__(other)

    def __ge__(self, other):
        return [ord(c) for c in self] <= [ord(c) for c in other]

    def __le__(self, other):
        return not self.__ge__(other)

    def __add__(self, other):
        return FuzzyString(str(self) + str(other))

    def __contains__(self, substring):
        return True if canonical_caseless(substring) in canonical_caseless(self) else False


if __name__ == '__main__':
    o_word = FuzzyString("ss, ß, \u7099, and \uf9fb")
    print(o_word.casefold())
    print('octo' in o_word.lower())
