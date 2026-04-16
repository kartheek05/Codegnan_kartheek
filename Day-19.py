'''
Modules---> A module is a pyhton is simply file that contains pyhton code(functions,variables,classes)
---> to use this modules, we have to use a keyword called (import) before the module.

---------------------------------------------------------------Types of modules----------------------------------------------
User-defines modules-----> This is developed by the user or programmer inside a file of pyhton code and used by called import
                                                with filename
Syntax -----> import(keyword) file_name
                     file_name.functionality
import add               #user-definedmodules
print(add.sub(4,5))
print(add.add(4,5))
print(add.mul(4,5))
print(add.div(4,5))
print(add.kartheek+3)
'''


'''
1.Build-IN or inbuilt-------------> already these modules will come with installation and they are ready to use in the program.
                                                  This are developed by the developers.
Syntax -----> import(random) module_name
                     module_name.functionality

import math
print(math.sqrt(16))                                                  
'''
import random
number = random.randint(1,10)
attempts = 3
while attempts > 0:
    user_num = int(input("Guess the number between 1 to 10 : "))
    if user_num == number:
        print("\nCongrants! You guessed it right")
        break
    else:
        attempts -= 1
        print(f"\nWrong Guess! Try again. Attempts remaining {attempts}\n")
        if attempts > 0:
            if  num > user_num :
                print("Hint : Guessed Number is more than Actual Number\n")
            else:
                print("Hint : Guessed Number is less than Actual Number\n")
if attempts <= 0:
    print(f"The number is {num}")
        





















