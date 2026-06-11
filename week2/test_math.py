import sys
sys.path.append('.')
from math_utils import square, is_even, sum_list

def test_square():
    assert square(2) == 4
    assert square(0) == 0
    assert square(-3) == 9

    print("Square test passed!")


def test_is_even():
    assert is_even(4) == True
    assert is_even(5) == False

    print("Is even test passed!")

def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([0]) == 5
    assert sum_list([]) == 0

    print("Sum list test passed!")

if __name__ == "__main__":
    test_square()
    test_is_even()
    test_sum_list()
    
    print("All tests passed!")