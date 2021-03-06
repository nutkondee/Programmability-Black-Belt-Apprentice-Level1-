"""
Libraries and Functions always come in handy to developers by allowing reusability of existing code. There are certain well known inherent libraries that you have access to after installing python. By using these libraries and functions in them, write a program (in Python 3) to guess a randomly generated number between 1 and 10.
For Example:

Guess the number: 4
Wrong, try again!

Guess the number: 8
Correct!

Hint: Figure out which library the randint function belongs to.

"""


import random

isCorrect = False
radnum = random.randint(1,10)
print ("system random number : {}".format(radnum))
while not isCorrect:
    try:
        inpnum = int(input("Guess the number : "))
        print ("system random number : {} | input number : {} ".format(radnum, inpnum))
        if inpnum == radnum:
            isCorrect = True
            print ("Correct!!!!")
    except:
        print ("Please enter number only [1-10]")
