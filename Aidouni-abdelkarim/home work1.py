#exo1:
student_info={"name":"alice","age":21,"grade":"B+"}



#exo2:
def get():
    name=str(input('please enter your name: '))
    age=int(input('please enter your age: '))
    grade=str(input('please enter your grade: '))
    student_inf={"name":name,"age":age,"grade":grade}
    while True:
        print("1.if you want to now the name of the student.")
        print("2.if you want to now the age of the student.")
        print("3.if you want to now the grade of the student.")
        print("4.if you want to now all student data.")
        print("5.Quit")
        choix=int(input("Choose an option : "))
        if choix==1:
            print(student_inf["name"])
        elif choix==2:
            print( student_inf["age"])
        elif choix==3:
            print(student_inf["grade"])
        elif choix==4:
            print( student_inf)
        elif choix==5:
            print("Good Bye!")
            break
        else:
            print("Invalid choice, please try again.")



#exo3:
def print_student_info(s_i:dict):
	for i in s_i:
		print(i,":",s_i[i])


#exo4:
class_information = {}
def ajouter_info():
	name = str(input('please enter your name: '))
	age=int(input('please enter your age: '))
	grade=str(input('please enter your grade: '))
	class_information[name]={"name":name,"age":age,"grade":grade}
	print(f"{name} successfully added.")


def print_info():
	i=str(input("please enter the name of the student: "))
	info=class_information.get(i)
	if info:
		print(f"name: {i}, age: {info['age']},grade: {info['grade']}")
		return
	else:
		print(f"The student {i} does not exist in class")
		return


