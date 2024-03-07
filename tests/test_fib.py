import pytest
from template_workshop import Fibonacci


def test_import():
    # This checks __init__ was set up correctly
    try:
        from template_workshop import Fibonacci
    except ImportError:
        assert False


##### YOUR CODE HERE #####
@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
    ],
)
def test_fib(n, expected):
    f = Fibonacci()
    assert f.fib(n) == expected


##########################
