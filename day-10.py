'''
#checking the number are prime or not 
num_ = int(input())
count = 0
for j in range(1,num_ + 1):
    if num_ % j == 0:
        count += 1
    if count > 2:
        break
if count == 2:
    print(f"{num_} is prime number")
else:
    print(f"{num_} is not a prime number")
<---------------------------------------------------------------------------------------------------->
#checking the number are prime or not 
num_1 = int(input())
num_2 = int(input())
count = 0
for j in range(num_1,num_ 2 + 1):
    if num_1 % j == 0:
        count += 1
    if count > 2:
        break
if count == 2:
    print(f"{num_} is prime number")
else:
    print(f"{num_} is not a prime number")
<---------------------------------------------------------------------------------------------------->
#checking the number are prime or not 
for an in range(2,100):
    count = 0
    for j in range(1,an+1):
        if an % j == 0:
            count += 1
    if count == 2:
        print(f"{an} is a prime")
    else:
        print(f"{an} is not a prime")
<---------------------------------------------------------------------------------------------------->
#checking the number are prime or not 
s = [1057,197,9 ,86,17673]
for an in s:
    count = 0
    for j in range(1,an+1):
        if an % j == 0:
            count += 1
    if count == 2:
        print(f"{an} is a prime")
    else:
        print(f"{an} is not a prime")
<---------------------------------------------------------------------------------------------------->
#generating even or odd numbers
for an in range(1,100+1):
    if an % 2 == 0:
        print(f"{an} is a even number")
    else:
        print(f"{an} is a Odd Number")
<---------------------------------------------------------------------------------------------------->
# Removing duplicates using new list
any = [2,356,8,6,3,2,8]
so = []
for j in any:
    if j not in so:
        so.append(j)
print(so)
<---------------------------------------------------------------------------------------------------->
so = int(input("Enter the Number: "))
length = len(str(so))
Amstr = 0
for j in str(so):
    Amstr += int(j) ** (length)
if Amstr == so:
    print(f"{so} is a Amstrong Num")
else:
    print(f"{so} is not a Amstrong Num")
'''   
# Take a list only with integers add all even numbers and add all the even numbers

        
