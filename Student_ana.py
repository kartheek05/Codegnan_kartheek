# Student Data Analyzer

def add_student():
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks (space separated): ").split()))
    
    total = sum(marks)
    avg = total / len(marks)

    # Grade calculation using lambda
    grade = (lambda a: "A" if a >= 90 else "B" if a >= 75 else "C" if a >= 50 else "Fail")(avg)

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": avg,
        "grade": grade
    }

    return student


def display_students(students):
    print("\n----- Student Report -----")
    for s in students:
        print(f"Name: {s['name']}")
        print(f"Marks: {s['marks']}")
        print(f"Total: {s['total']}")
        print(f"Average: {s['average']:.2f}")
        print(f"Grade: {s['grade']}")
        print("-" * 30)


def topper(students):
    top = max(students, key=lambda x: x['average'])
    print(f"\nTopper: {top['name']} with {top['average']:.2f}")


def passed_students(students):
    passed = [s for s in students if s['grade'] != "Fail"]
    print(f"\nPassed Students: {[s['name'] for s in passed]}")


# Main Program
students = []

n = int(input("Enter number of students: "))

for _ in range(n):
    students.append(add_student())

display_students(students)
topper(students)
passed_students(students)