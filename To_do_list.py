'''Display a welcoming message and a menu with the following options:
Welcome to the To-Do List App!

Menu:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Quit'''

class NotFoundError(Exception):
    def __init__(self, message):
        self.message = message

def home_page():
    print("\nWelcome to the To-Do List App!\n")
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")
    print("0. Back to home screen\n")


def add_task():
    incomplete = 'incomplete'
    user_input = str(input("\nPlease enter the task you would like to add: "))
    task = user_input + ': ' + incomplete 
    return task



def  view_task(list):
    i = 1
    print("\nThese are your current tasks:")
    if list == []:
        print("You have nothing added!")
    else:
        for task in list:
            print(f"{i}. {task}")
            i += 1

def make_complete(list):
    while True:
        user_input = input("\nGreat job! Which task have you completed today? If you change your mind, type '0' to go back ")
        if user_input + ': ' + 'incomplete'  in list:
            list.remove(user_input + ': ' + 'incomplete')
            list.append(user_input + ': ' + 'complete')
            break
        elif user_input == '0':
            break
        else:
            print("Looks like the choice you have given is not in the list. Please type your task exactly the same as you added!")

                

def delete_task(list):
     while True:
        user_input = input("\nWhich task would you like to delete? If you change your mind, type '0' to go back ")
        if user_input + ': ' + 'incomplete'  in list:
            list.remove(user_input + ': ' + 'incomplete')
            break
        elif user_input + ': ' + 'complete' in list:
            list.remove(user_input + ': ' + 'complete')
            break
        elif user_input == '0':
            break
        else:
            print("Looks like the choice you have given is not in the list. Please type your task exactly the same as you added!")


added_tasks = []
home_page()
while True:


    try:
        user_input = int(input("\nWhich number would you like to choose? "))      
        if user_input > 5 or user_input < 0:
            raise ValueError("\nINVALID NUMBER. TRY AGAIN!\n")
    except NotFoundError as ne:
            print(ne)
    except ValueError:
            print("\nPLEASE ENTER A NUMBER LISTED ABOVE.\n")
    else:
        if user_input == 1:
            added_task = add_task()
            added_tasks.append(added_task)
        elif user_input == 2:
            view_task(added_tasks)
        elif user_input == 3:
            make_complete(added_tasks)
        elif user_input == 4:
            delete_task(added_tasks)
        elif user_input == 5:
            break
        elif user_input == 0:
            home_page()
    finally:
        print("\nThanks for your time today! Hope to see you again soon.")