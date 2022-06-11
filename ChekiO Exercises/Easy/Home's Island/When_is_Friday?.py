"""Friday is an awesome day. It's the end of the week after which you can just relax and attend to all of the things you've been pushing away. It's really good to know how many days you still have to wait, isn't it?

Your task is to write a function that will count how many days are left from a certain date to Friday. The argument will be a particular date in a string format looking like this: 'dd.mm.yyyy', where 'dd' - day, 'mm' - month, and 'yyyy' - year.
For example, if that given day is Thursday, then the answer will be 1. If that day is Monday, the result is 4. And if that day is Friday, the function should return 0.

example

Input: Date as a string.

Output: The amount of days left until Friday.

Example:

friday('23.04.2018') == 4
friday('01.01.1999') == 0 """


import datetime
def friday(day):
    #replace this for solution
    for n,x in enumerate(day.split('.')):
        if n == 0:
            day = int(x)
        elif n == 1:
            month = int(x)
        else:
            year = int(x)
    
    day_n = int(datetime.datetime(year, month, day).strftime("%w"))
    
    if day_n == 6:
        return 6
    else:
        return 5 - day_n

if __name__ == '__main__':
    print("Example:")
    print(friday('23.04.2018'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert friday('23.04.2018') == 4
    assert friday('01.01.1999') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")

