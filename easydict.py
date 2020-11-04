
class EasyDict:
    def __init__(self, mapping=None, normalize=False, **kwargs):
        if mapping is None:
            mapping = {}
        self._normalize = normalize
        for key, value in mapping.items():
            self[key] = value
        for key, value in kwargs.items():
            self[key] = value

    def normalized(self, key):
        return key.replace(" ", "_") if self._normalize else key

    def __getitem__(self, key):
        return getattr(self, self.normalized(key))

    def __setitem__(self, key, value):
        setattr(self, self.normalized(key), value)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get(self, key, default=None):
        return getattr(self, self.normalized(key), default)


if __name__ == '__main__':
    d = EasyDict({'greeting 1': 'hi'}, normalize=True)
    print(d.__dict__)
