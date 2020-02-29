todos = []
stop = False

def get_todos():
    global todos
    return todos

def add_one_task(title):
    global todos
    todos.append(title)

def print_list():
    global todos
    k=1
    for data in todos:
        print(k,data)
        k=k+1

def delete_task(number_to_delete):
    global todos
    number_to_delete=int(number_to_delete)-1
    todos.pop(number_to_delete)
    print_list()

def save_todos():
    global todos
    file = open('tareas.txt', 'w')
    for data in todos:
        file.write(data+'\n')
    file.close()
    print('done')

def load_todos():
    global todos
    todos=[]
    file=open('tareas.txt','r')
    for row in file:
        row=row.replace('\n','')
        if row!='':
            todos.append(row)
    print('done')

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input('*** menu: ')
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            number_to_delete = input("What task number you want to delete? ")
            delete_task(number_to_delete)
        elif response == "1":
            title = input("What is your task title? ")
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")