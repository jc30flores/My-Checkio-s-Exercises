"""Your task in this mission is to truncate a sentence to a length that does not exceed a given number of characters.

If the given sentence already is short enough, you don't have to do anything to it. But if it needs to be truncated, the omission must be indicated by concatenating an ellipsis ("...") to the end of the shortened sentence.

The shortened sentence can contain complete words and spaces.
It must neither contain truncated words nor trailing spaces.
The ellipsis has been taken into account for the allowed number of characters, so it does not count against the given length.

Input: Two arguments:

one-line sentence as a string,
max length of the truncated sentence as an int.
Output: The shortened sentence plus the ellipsis (if required) as a one-line string.

Examples:

cut_sentence("Hi my name is Alex", 4) == "Hi..."
cut_sentence("Hi my name is Alex", 8) == "Hi my..."
cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"
cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex" """


def cut_sentence(line: str, length: int) -> str:
    '''
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    '''
    
    # your code here
    new_line = ''
    #In this condition drop the last word in the line if it is a cut word and return the others words with "..."
    if line[:length].split(' ')[-1] not in line.split(' '):
        for x in line[:length].split(' ')[:-1]:
            new_line += x + ' ' #Add the word that is complete with a space in new_line
        return new_line[:-1] + '...' #Remove the last space and add three dots.
    
    
    else:
        #Here just check if the line with the limit is equal to the initial line.
        if line[:length].split(' ')[-1] == line.split(' ')[-1]:
            return line
        
        #And if the line hasn't words cut, return the line with its respective limit with three dots.
        else:
            return line[:length] + '...'   
            

cut_sentence("Hi my name is Alex", 4)
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
    assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
    assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
    assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
    print('Done! Do you like it? Go Check it!')

