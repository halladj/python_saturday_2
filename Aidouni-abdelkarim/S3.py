# class TodoList:
#     co=0
#     def __init__(self):
#         self.DB={}
#     def PrintTasks(self):
#         for key in self.DB:
#             print(key)
#
#
# instance = TodoList()
# instance2 = TodoList()
#
# instance.DB["key"]="value"
# instance2.DB
#
#
# print(instance.DB)
# print(instance2.DB)
#
#
#
#
#
#
# class Dog:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         print(f"{self.name} woof!")
#
# instane= Dog("Dog", 10)
# instane.bark()
#

#
class SpecialList:
    def __init__(self):
        self.my_list = []
    def add(self, item):
        self.my_list.insert(0,item)

    def find(self, item):
        if item in self.my_list:
            return True
        return False
    def access(self):
        return self.my_list[0]
    def max(self):
        for item in self.my_list:
            for item2 in self.my_list:
                if item > item2:
                    return item
    def min(self):
        for item in self.my_list:
            for item2 in self.my_list:
                if item > item2:
                    return item2
                


alist = SpecialList()
alist.add("qqqqw")
alist.add("q")
alist.add("qqq")







