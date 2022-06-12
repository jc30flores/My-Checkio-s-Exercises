"""Your task is to encrypt the text message using the Morse code . The input text will consist of letters (in uppercase and lowercase), numbers and whitespaces. There won't be any special characters ('&', '?', '#' etc.)
You need to use 3 spaces between words and 1 space between each letter of each word.

example

Input: The secret message as a string.

Output: The same string, but encrypted.

Example:

morse_encoder("some text") == "... --- -- .   - . -..- -"
morse_encoder("2018") == "..--- ----- .---- ---.."
morse_encoder("It was a good day") == ".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--" """


MORSE = {'a': '.-',    'b': '-...',  'c': '-.-.',
         'd': '-..',   'e': '.',     'f': '..-.',
         'g': '--.',   'h': '....',  'i': '..',
         'j': '.---',  'k': '-.-',   'l': '.-..',
         'm': '--',    'n': '-.',    'o': '---',
         'p': '.--.',  'q': '--.-',  'r': '.-.',
         's': '...',   't': '-',     'u': '..-',
         'v': '...-',  'w': '.--',   'x': '-..-',
         'y': '-.--',  'z': '--..',  '0': '-----',
         '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.'
        }

def morse_encoder(text):
    #replace this for solution
    text_morse = '' 
    text = text.lower().split()
    for word in text:
        for l in word:
            text_morse += MORSE[l] + ' '
        text_morse += '  '
    
    return text_morse[:-3]

if __name__ == '__main__':
    print("Example:")
    print(morse_encoder('some text'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_encoder("some text") == "... --- -- .   - . -..- -"
    assert morse_encoder("2018") == "..--- ----- .---- ---.."
    assert morse_encoder("It was a good day") == ".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"
    print("Coding complete? Click 'Check' to earn cool rewards!")
