"""Your function should return the length of the given string

Input: String.

Output: Int.

Example:

assert string_length("hi") == 2
assert string_length("CheckiO") == 7
assert string_length("") == 0 """

def string_length(text: str) -> int:
    # your code here
    return len(text)


print("Example:")
print(string_length("Hi"))

assert string_length("hi") == 2
assert string_length("CheckiO") == 7
assert string_length("") == 0

print("The first mission is done! Click 'Check' to earn cool rewards!")
