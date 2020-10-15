from collections import namedtuple
from functools import wraps

NO_RETURN = object()


def record_calls(func):
    Call = namedtuple('calls', ['args', 'kwargs', 'return_value', 'exception'])

    @wraps(func)
    def helper(*args, **kwargs):
        helper.call_count += 1
        try:
            res = func(*args, **kwargs)
        except Exception as e:
            helper.calls.append(Call(args, kwargs, NO_RETURN, e))
            raise
        else:
            helper.calls.append(Call(args, kwargs, res, None))
        return res

    helper.calls = []
    helper.call_count = 0
    return helper


def main():
    @record_calls
    def greet(name):
        print(f"Hello {name}")

    greet('mike')
    greet('bill')
    print(greet.call_count)
    print(greet.calls[0].args)


if __name__ == '__main__':
    main()
