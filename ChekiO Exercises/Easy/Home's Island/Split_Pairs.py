"""Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.

Output: An iterable of strings.

Example:

split_pairs('abcd') == ['ab', 'cd']
split_pairs('abc') == ['ab', 'c_'] """


def split_pairs(a):
    # your code here
    pair = []
    if len(a)%2 == 1:
        a += "_"
    if len(a) == 2:
        pair.append(a[:2])
            
    elif len(a) == 4:
        pair.append(a[:2])
        pair.append(a[2:5])
            
    elif len(a) == 6:
        pair.append(a[:2])
        pair.append(a[2:4])
        pair.append(a[4:6])
            
    elif len(a) == 8:
        pair.append(a[:2]) 
        pair.append(a[2:4])
        pair.append(a[4:6])
        pair.append(a[6:8])
    return pair


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
