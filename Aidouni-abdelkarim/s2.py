import json
from pathlib import Path



FILE_NAME= "tasks.json"
FILE_PATH=Path("",FILE_NAME)
DB={}



def add(task):
	DB[f"task-{len(DB)}"]=task
	with open(FILE_PATH,"w") as file:
		json.dump(DB,file)


def creat_task():
	taskname =input('please enter task_name:')
	taskpriority =input('please enter task-priority:')
	task={"task-name":taskname,"priority":taskpriority}
	return task


def print_task():
	with open(FILE_PATH,"r") as file:
		DB=json.load(file)
	for k,v in DB.items():
		print(f"{k}:{v}")



def delete(task_key):

	del DB[task_key]
	with open(FILE_PATH,"w") as file:
		json.dump(DB,file)


def GetOneTask():
	with open(FILE_PATH,"r") as file:
		DB=json.load(file)
	for k,v in DB.items():
		print(f"{k}:{v}")
	try:
		task_id=input("please enter task_id: ")
		print(DB[task_id])
	except KeyError:
		print("please enter a valid task name")

if __name__=="__main__":

	try:
		with open(FILE_PATH, "x") as file:
			pass
	except:
		pass

	with open(FILE_PATH,"r") as file:
		DB=json.load(file)
	while True:
		print("1.to creat task.")
		print("2.to print task.")
		print("3.to print one task.")
		print("4.to delete task.")
		print("5.Quit.")
		a=int(input('please enter your choice:'))
		if a==1:
			add(creat_task())
		elif a==2:
			print_task()
		elif a==3:
			GetOneTask()
		elif a==4:
			try:
				key=input("enter task-key: ")
				delete(key)
				print(f"the {key} has delete ")
			except :
				print('key dosnt exx')
		elif a==5:
			break
		else:
			print('error!!!')


