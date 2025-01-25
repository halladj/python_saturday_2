# try:
# 	with open("TEST.txt","x") as f:
# 		pass
# except :
# 	print('Error:file already Exists')
# fille_Name='TEST.txt'
# with open(fille_Name,'r') as f:
# 	for item in f.readline():
# 		print(item)


DB={}
def add(task):
	DB[f"task-{len(DB)}"]=task

def creat_task():
	taskname =input('please enter task_name:')
	taskpriority =input('please enter task-priority:')
	task={"task-name":taskname,"priority":taskpriority}
	return task
def print_task():
	for k,v in DB.items():
		print(f"{k}:{v}")
def delete(task_key):
	del DB[task_key]

while True:
	print("1.to creat task.")
	print("2.to print task.")
	print("3.to delete task.")
	print("4.Quit.")
	a=int(input('please enter your choice:'))
	if a==1:
		add(creat_task())
	elif a==2:
		print_task()
	elif a==3:
		try:
			key=input("enter task-key: ")
			delete(key)
			print(f"the {key} has delete ")
		except :
			print('key dosnt exx')
	elif a==4:
		break
	else:
		print('error!!!')
