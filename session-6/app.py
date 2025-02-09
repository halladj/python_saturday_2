import json
from pathlib import Path
FILE_NAME=  "tasks.json"
FILE_PATH = Path("session-6", FILE_NAME)
DB= {}

def add_task(task):
    DB[f"task-{len(DB)}"] = task
    # save task in json-file.
    with open(FILE_PATH, "w") as f:
        json.dump(DB, f)

def create_task():
    taskname     = input("Please enter task-name: ")
    taskpriority = input("Please enter task-priority: ")
    
    task = {"task-name": taskname, "priority": taskpriority}
    return task

def print_tasks():
    #  TODO: read tasks from json file.
    with open (FILE_PATH, "r") as f:
        DB = json.load(f)

    for k,v in DB.items():
        print(f"{k}: {v}")

def delete_task(task_key):
    del DB[task_key]
    # save task in json-file.
    with open(FILE_PATH, "w") as f:
        json.dump(DB, f)


## TODO: create a GetOneTask function, to print
##       a task, using a task-id.
def GetOneTask(task_id):
    # 1- load json file.
    with open(FILE_PATH, "r")as f:
        DB = json.load(f)
    try:
        return DB[task_id]
    except:
        print("task-id NOT FOUND")


if __name__ == '__main__':
    try:
        with open(Path("session-6",FILE_NAME), "x") as f:
            pass
    except:
        pass

    while True:
        #  TODO: read tasks from json file.
        with open (FILE_PATH, "r") as f:
            DB = json.load(f)
        
        option = ""
        print("PRESS the associated number..")
        print("(1) Add new-task..")
        print("(2) print all-tasks..")
        print("(3) Delete a task..")
        print("(4) Get one task by ID..")
        print("(5) quit the app..")
        option = int(input())
        if option == 1:
            add_task(create_task())
        elif option == 2:
            print_tasks()
        elif option == 3:
            try:
                key = input("please enter they task-key: ")
                delete_task(key)
            except:
                print("Invalid key.....")
        elif option == 4:
            print_tasks()
            task_id = input("enter task id")
            print(GetOneTask(task_id))
        elif option == 5:
            break
                
         