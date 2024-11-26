
todo_list = []

def add_task():
    tasks=input('Enter your task: ')
    todo_list.append(tasks)
    print(f'{tasks} added in a To-do list')

def remove_task():
    task_to_remove=input('Enter the task to remove: ')
    if task_to_remove in todo_list:
        todo_list.remove(task_to_remove)
        print(f'{task_to_remove} has been deleted.')
    else:
        print(f'{task_to_remove} not found in To-do list.')
    
def view_task():
    if not todo_list:
        print('To-do list is empty' )
    else:
        print('Your To-do list:')
        for i in range(len(todo_list)):
            print(f'{i+1}. {todo_list[i]}')

    
def main():
    while True:
        print('1. Add Task')
        print('2. Remove Task')
        print('3. View Task')
        print('4. Quit')
        print()

        choice=int(input('Enter Your Choice: '))
        print()
        if choice == 1:
            add_task()
            print()
        elif choice == 2:
            remove_task()
            print()
        elif choice == 3:
            view_task()
            print()
        elif choice == 4:
            print("Exiting the To-do app")
            print()
            break
        else:
            print('Envalid Input')


main()