# Student List Manager using List Methods

print("----- Student List Manager -----")

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    students.append(name)

print("\nStudent List:", students)

pos = int(input("\nEnter position to insert new student: "))
new_student = input("Enter new student name: ")
students.insert(pos, new_student)

print("After insert:", students)

remove_name = input("\nEnter student name to remove: ")
if remove_name in students:
    students.remove(remove_name)
    print("After removal:", students)
else:
    print("Student not found!")

search_name = input("\nEnter name to count: ")
print("Count:", students.count(search_name))

students.sort()
print("\nSorted List:", students)

students.reverse()
print("Reversed List:", students)

copy_list = students.copy()
print("\nCopied List:", copy_list)

students.clear()
print("After clear:", students)
