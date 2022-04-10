""" In a given string you should reverse every word, but the words should stay in their places.

Input: A string.

Output: A string.

Example:
backward_string_by_word('') == ''
backward_string_by_word('world') == 'dlrow'
backward_string_by_word('hello world') == 'olleh dlrow'
backward_string_by_word('hello   world') == 'olleh   dlrow'

Precondition: The line consists only from alphabetical symbols and spaces. """

def backward_string_by_word(text: str) -> str:
    # your code here
    new = []
    #The loop take each word and reverse it.
    for t in text.split(' '):
        new.append(t[::-1])
    #Convert each element in new to a str and separate with a space.
    new_text = " ".join(new)
    return new_text


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")