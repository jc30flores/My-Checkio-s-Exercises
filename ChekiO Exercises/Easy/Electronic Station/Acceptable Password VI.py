"""In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.
a string should not contain the word "password" in any case;
should contain at least 3 different letters (or digits) even if it is longer than 10
Input: A string.

Output: A bool.

Example:

is_acceptable_password('short') == False
is_acceptable_password('short54') == True
is_acceptable_password('muchlonger') == True
is_acceptable_password('ashort') == False
is_acceptable_password('muchlonger5') == True
is_acceptable_password('sh5') == False
is_acceptable_password('1234567') == False
is_acceptable_password('12345678910') == True
is_acceptable_password('password12345') == False
is_acceptable_password('PASSWORD12345') == False
is_acceptable_password('pass1234word') == True
is_acceptable_password('aaaaaa1') == False
is_acceptable_password('aaaaaabbbbb') == False """


def is_acceptable_password(password: str) -> bool:
    digit = 0
    #Este bucle es para contar la cantidad de numeros que lleva password; en digit
    for p in password:
        if p.isdigit():
            digit += 1
    #Este bucle es para contar la cantidad de letras y digitos unicos que lleva password; en count
    count = {'letter': 0, 'digit': 0}
    for i in list(set(password)):
        if i.isdigit():
            count['digit'] += 1
        else:
            count['letter'] += 1
    
    #La password no puede contener la palabra password, uso .lower() por si la palabra es puesta en upper, title, or mixer       
    if "password" in password.lower():
        return False
    
    #The password que sea len(password) > 9 y tenga al menos 3 digitos o letras diferentes puede omitirse las siguientes reglas
    elif len(password) > 9 and (count['digit'] >= 3 or count['letter'] >=3):
        return True
    
    #The password debe ser > 6, at least one digit, no contener solo digitos y contener al menos 3 digitos o letras diferentes
    elif len(password) > 6 and digit >= 1 and not password.isdigit() and count['letter'] + count['digit'] >= 3:
        return True
    
    else:
        return False
    
if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    assert is_acceptable_password("password12345") == False
    assert is_acceptable_password("PASSWORD12345") == False
    assert is_acceptable_password("pass1234word") == True
    assert is_acceptable_password("aaaaaa1") == False
    assert is_acceptable_password("aaaaaabbbbb") == False
    assert is_acceptable_password("aaaaaabb1") == True
    assert is_acceptable_password("abc1") == False
    assert is_acceptable_password("abbcc12") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")

