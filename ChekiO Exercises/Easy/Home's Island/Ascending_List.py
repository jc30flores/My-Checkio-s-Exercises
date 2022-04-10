""" Determine whether the sequence of elements items is ascending 
such that each of its elements is strictly larger than (and not merely equal to) the preceding element.

Input: Iterable with ints.

Output: Bool.

Example:

is_ascending([-5, 10, 99, 123456]) == True
is_ascending([99]) == True
is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
is_ascending([]) == True
is_ascending([1, 1, 1, 1]) == Falses

The mission was taken from Python CCPS 109 Fall 2018. 
It is taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen. """

from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
    # your code here
    count = 0
    
    if len(items) == 0:
        return True
    #Check if each element except last one, is shorter than the next then sum 1 to count if that element is right.
    for i in range(0, len(items)-1):
        if items[i] < items[i+1]:
            count += 1
    #If all the elements are right the count is equal to the number of elements - 1 in items.
    if count == len(items) -1:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")