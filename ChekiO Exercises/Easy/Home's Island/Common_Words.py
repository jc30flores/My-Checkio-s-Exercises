"""Let's continue examining words. You are given two strings with words separated by commas. Try to find what is common between these strings. The words in the same string don't repeat.

Your function should find all of the words that appear in both strings. The result must be represented as a string of words separated by commas in alphabetic order.

Input: Two arguments as strings.

Output: The common words as a string.

Example:

checkio('hello,world', 'hello,earth') == 'hello'
checkio('one,two,three', 'four,five,six') == ''
checkio('one,two,three',
 'four,five,one,two,six,three') == 'one,three,two' """
 
 
 def checkio(line1: str, line2: str) -> str:
    # your code here
    count = {}
    for w in str(line1 + ',' + line2).split(','):
        if w in count:
            count[w] += 1
        else:
            count[w] = 1
    words_sorted = sorted(list(w for w,c in count.items() if c > 1))
    result = ''
    for w in words_sorted:
        if w == words_sorted[-1]:
            result += w
        else:
            result += w + ','
    return result

if __name__ == '__main__':
    print("Example:")
    print(checkio('hello,world', 'hello,earth'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three',
 'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")
