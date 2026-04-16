'''a = input("Enter the sentence: ").lower()
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

any_ = "Pyhton is a programming language"
vowel_cou = 0
space_cou = 0
for  j in any_:
    if j in "Aeiouaeiou":
        vowel_cou += 1
    elif j == " ":
        space_cou += 1
print(f"This is count of all vowel o=in the string {vowel_cou}")
print(f"This is the count of all space in the string {space_cou}")
print(f"This is count of all cons_ in the string {len(any_) - (vowel_cou + space_cou)}")
'''
