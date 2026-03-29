a = input("Enter the sentence: ").lower()
count_1 = 0
count_2 = 0
count_3 = 0
for i in a :
    if  i in "a,e,i,o,u" :
        count_1 += 1
    elif i in " ":
        count_3 += 1
    else:
        count_2 += 1
print(f"The Total no of Vowels are {count_1} and Total no.of Consonants are {count_2} and Total No of Spaces given are {count_3}")
