""" (At the top right of the mission description there is always a list of available translations)

This is an intro mission, the purpose of which is to explain how to solve missions on CheckiO and how to get the most out of solving them. As you solve missions more stations become available to you, containing more complex missions.

This mission is the easiest one. Write a function that will receive 2 numbers as input and it should return the multiplication of these 2 numbers.

Input: Two arguments. Both are of type int.

Output: Int.

Example:

mult_two(2, 3) == 6
mult_two(1, 0) == 0 """

def mult_two(a, b):
    return a * b


if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
