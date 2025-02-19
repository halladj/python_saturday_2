import json
from pathlib import Path1
FILE_NAME = "task.json"
FILE_PATH = Path("mouatez", FILE_NAME)
#FILE_PATH = Path("C:\Users\Chaker Officiel\Desktop\Mouatez\python_course\python_saturday_2\mouatez", FILE_NAME)
DB= {}

try :
    with open(FILE_PATH,'x') as f:
        pass
except:
    pass

def add_task(task):
    DB[f"task-{len(DB)}"] = task
    # TODO: save DB in json file.
    with open(FILE_PATH,'w') as f:
        json.dump(DB,f)


def create_task():
    taskname     = input("Please enter task-name")
    taskpriority = input("Please enter task-priority")
    
    task = {"task-name": taskname, "priority": taskpriority}
    return task

def print_tasks():
    # TODO: load from json file.
    with open(FILE_PATH,'r') as file:
        json_object = json.load(file)
    for k,v in DB.items():
        print(f"{k}: {v}")

def delete_task(task_key):
    del DB[task_key]

#TODO : crate a GetOneTask function,to print a task using a task-id
def GetOneTask(task_id):
    with open(FILE_PATH,"r") as f:
        DB = json.load(f)
    try:
        return DB[task_id]
    except:
        print("task_id NOT FOUND")

if __name__ == '__main__':
    print(FILE_PATH)
    # TODO: load from json file.
    with open(FILE_PATH,'r') as f:
        json_object = json.load(f)
    while True:
        option = ""
        print("PRESS the associated number..")
        print("(1) Add new-task..")
        print("(2) print all-tasks..")
        print("(3) Delete a task..")
        print("(4) get one task by it's id..")
        print("(5) quit the app..")
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
            print_tasks()
            task_id = input("enter task id : ")
            print(GetOneTask(task_id))
        elif option == 5:
            break;
                
         