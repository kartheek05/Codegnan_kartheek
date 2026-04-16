#String Methods ----->
#There are several methods in string(strip,replace,capital,lower)

name = " kaRTHEEKis a programminglanguage "

print(name.replace("a","b"))#here it will replace the letters which are given.
print(name.casefold())# here it will convert the letters into loewr case letters both latin and normal letters.
print(name.lower()) #here it will convert the lettres to smaller case.
print(name.upper())#here it will convert the letters into the upper case.
print(name.count("E"))#Here it will count the given letter which we give from the variable.
print(name.isalpha())#here it will check the only letters in the given variable.
print(name.capitalize())#here it will convert the first letter into capital in the variable.
print(name.index("K"))#Here it will give the index value of given thing.
print(name.split("g"))#
print(name.title())#it will convert the first letter of every word.
print(name.lstrip(" "))#it will remove the left space of string.
print(name.rstrip(" "))#it will remove the right space of string.
print(name.islower())#it will check it is lower or not .
print(name.isupper())#it will check it is upper or not.

