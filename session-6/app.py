DB= {}

def add_task(task):
    DB[f"task-{len(DB)}"] = task

def create_task():
    taskname     = input("Please enter task-name")
    taskpriority = input("Please enter task-priority")
    
    task = {"task-name": taskname, "priority": taskpriority}
    return task

def print_tasks():
    for k,v in DB.items():
        print(f"{k}: {v}")

def delete_task(task_key):
    del DB[task_key]

if __name__ == '__main__':
    while True:
        option = ""
        print("PRESS the associated number..")
        print("(1) Add new-task..")
        print("(2) print all-tasks..")
        print("(3) Delete a task..")
        print("(4) quit the app..")
        option = int(input())
        if option == 1:
            add_task(create_task())
        elif option == 2:
            print_tasks()
        elif option == 3:
            try:
                key = input("please enter they task-key")
                delete_task(key)
            except:
                print("Invalid key.....")
        elif option == 4:
            break;
                
         