filename = "list_task.txt"


def read_file():
    f = open(filename, "r")
    return f.readlines()


def write_file(task):
    f = open(filename, "a")
    f.write(f"{task}\n")


def menu():
    print("Enter you type operation")
    print("Enter 1 if you want to add a task")
    print("Enter 2 if you want delete the task and add it to the completed list")
    print("Enter 3 if you want to see a list of tasks")
    print("Enter 4 if you want to see a list of completed tasks")
    print("Enter q if you want to quit")
    option = input("Enter your choice: ")
    return option


def add():
    task = input("Enter a new task: ")
    write_file(task)


def complete():
    delete = int(input("Select a task that you have completed and it will be removed from the list: "))
    if delete <= len(list_task):
        element = list_task.pop(delete - 1)
        task_complete.append(element)
    else:
        print("Invalid value")


list_task = read_file()
task_complete = []

while True:
    choice = menu()
    if choice == '1':
        add()
    elif choice == '2':
        for i, number in enumerate(list_task):
            print(f" {i + 1}. {number}")
        complete()
    elif choice == '3':
        if not list_task:
            print("The list is empty")
        for i, number in enumerate(list_task):
            print(f"{i + 1}. {number}")
    elif choice == '4':
        if not task_complete:
            print("The list is empty")
        for i, number in enumerate(task_complete):
            print(f"{i + 1}. {number}")
    elif choice == 'q':
        break
    else:
        print("Invalid value")
