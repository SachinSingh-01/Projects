'''To-Do List Application (Easy → Moderate)
What to build
Add tasks
Remove tasks
View all tasks
Concepts used
List to store tasks
Loop to show tasks
match-case for user choice
Functions for add, delete, display
Strings for task descriptions
if-else for empty list handling'''
task=[]
print("1. Add task")
print("2. Delete task")
print("3. Display task")
print("4. Exit")
def add_task(add):
    adds=input("Enter the task: ")
    task.append(adds)
def dis_task(display):
    if task==[]:
        print("No task is present")
    else: 
        for i in range(len(task)):
            print(f"{i+1}. {task[i]}")
def del_task(delete):
    if task==[]:
        print("Nothing to delete")
    else:
        n=int(input("Enter the task number you want to delete:"))
        task.pop(n - 1)
        print("Task deleted successfully")
while True:
    choose=int(input("Enter your choice(1-4):"))
    match choose:
        case 1:
            add_task(None)
        case 2:
            del_task(None)
        case 3:
            dis_task(None)
        case 4:
            break

