'''Contact Book System (Moderate)
What to build
Add contact (name, phone)
Search contact
Delete contact
Concepts used
Dictionary for contacts
Functions for CRUD operations
Loop for repeated menu
match-case for menu
Strings for names and numbers'''
contact={}
def add_contact(contacts):
    name=input("Enter your name:")
    number=int(input("Enter you phone number:"))
    contacts[name]=number
def search_contact(contacts):
    name=input("Enter your name:")
    if name in contacts:
        print(contacts[name])
    else:
        print("contact not found")
def delete_contact(contacts):
    name=input("Enter your name:")
    if name in contacts:
        contacts.pop(name)
    else:
        print("contact not found")
while True:
    print("\n1.Add")
    print("\n2.Search")
    print("\n3.Delete")
    print("\n4.Exit")
    choose=int(input("Enter the number between (1-4):"))
    match choose:
        case 1:
            add_contact(contact)
        case 2:
            search_contact(contact)
        case 3:
            delete_contact(contact)
        case 4:
            print("You Exit")
            break
        