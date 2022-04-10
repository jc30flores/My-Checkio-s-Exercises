""" You need to count how many non-empty lines a given text has.

An empty line is a line without symbols or the one that contains only spaces.

Input: A text.

Output: An int.

Example:

non_empty_lines('one simple line') == 1
non_empty_lines('') == 0
non_empty_lines('\nonly one line\n            ') == 1
non_empty_lines('''
Lorem ipsum dolor sit amet,

consectetur adipiscing elit
Nam odio nisi, aliquam
            ''') == 3 """

def non_empty_lines(text: str) -> int:
    # your code here
    count = 0
    #Convert each line in elements of a list.
    for t in text.splitlines():
        #If the element/line is a space or is empty just pass it
        if t.isspace() or not t:
            pass
        else:
            count += 1
    return count

if __name__ == '__main__':
    print("Example:")
    print(non_empty_lines('one simple line\n'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert non_empty_lines('one simple line\n') == 1
    assert non_empty_lines('') == 0
    assert non_empty_lines('\nonly one line\n            ') == 1
    assert non_empty_lines('''
Lorem ipsum dolor sit amet,

consectetur adipiscing elit
Nam odio nisi, aliquam
            ''') == 3

    print("Coding complete? Click 'Check' to earn cool rewards!")