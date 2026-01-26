'''Library Management Mini System (Moderate)
What to build
Issue book
Return book
Show available books
Concepts used
List for available books
Dictionary for issued books
match-case for actions
if-else for availability
Functions for issue and return'''
ava_book=["python course","AI/ML learning","Atomic habit","DSA in python","No one cares"]
issue_book={}
def issue_a_book():
    book_name=input("Enter the name of the book:")
    person_name=input("Enter your name:")
    if book_name in ava_book:
        ava_book.remove(book_name)
        issue_book[book_name] = person_name
        print("Book issued successful")
    else:
        print("Book not avaiable")
def return_a_book():
    return_book=input("Enter the book you want to return:")
    if return_book in issue_book:
        issue_book.pop(return_book)
        ava_book.append(return_book)
        print("Book returned successful")
    else:
        print("This book was not issued")
print("\n1.Issue book")
print("\n2.Return book")
print("\n3.Show available books")
print("\n4.Exit")
while True:
    choose=int(input("Enter the number from (1-4):"))
    match choose:
        case 1:
            issue_a_book()
        case 2:
            return_a_book()
        case 3:
            print("Available books are:")
            for book in ava_book:
                print("-", book)
        case 4:
            break
        case _:
            print("Invalid choice")