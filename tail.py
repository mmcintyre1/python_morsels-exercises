from collections import deque
from typing import Any, Iterable, List


def tail(data: Iterable, last_n_items: int) -> List[Any]:
    """
    Takes an iterable and returns the last_n_items
    of the iterable in a list.  If n is negative, returns
    an empty list.
    :param data: an iterable
    :param last_n_items: the last n items to return
    :return: a list
    """
    if last_n_items <= 0:
        return []
    return list(data)[-last_n_items:]


def tail_with_deque(data: Iterable, last_n_items: int) -> List[Any]:
    """
    An implementation of the tail function using deque.
    Solves the problem of copying the entire data variable
    into a list to iterate.
    :param data: an iterable
    :param last_n_items: the last n items to return
    :return: a list
    """
    if last_n_items <= 0:
        return []
    return list(deque(data, maxlen=last_n_items))


if __name__ == '__main__':
    squares = (n ** 2 for n in range(10000000))
    print(tail('hello', 2))
    # print(tail(squares, 3))
    print(tail_with_deque(squares, 3))
