from contextlib import ContextDecorator, contextmanager


class suppress(ContextDecorator):
    def __init__(self, *args):
        self.suppressed_errors = args
        self.traceback = None
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception, traceback):
        self.traceback = traceback
        self.exception = exception
        # using a type check here won't work with object inheritance
        return isinstance(exception, self.suppressed_errors)


# another solution without a class
# also contextmanager has a suppress ability, so
# we could use from contextmanager import suppress
@contextmanager
def suppress_2(*exception_types):
    try:
        yield
    except exception_types:
        pass


if __name__ == '__main__':
    with suppress(ValueError) as s:
        raise ValueError
