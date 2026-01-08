'''Student Grade Management System (Easy)
What to build
Store student names and their marks.
Calculate grade based on marks.
Show pass or fail.'''
def calculate_grade(marks):
    if (marks>90):
        return 'A'
    elif (marks>75):
        return 'B'
    elif (marks>60):
        return 'C'
    elif (marks>40):
        return 'E'
    else:
        return 'fail'
student={
    "Sachin":78,
    "Moni":67,
    "Sony":78,
    "Kumod":67
}
for name,marks in student.items():
    grade=calculate_grade(marks)
    if grade=="fail":
        result="Fail"
    else:
        result="pass"
    print(f"name:{name} marks:{marks} grade:{grade} result:{result}")