class TodoList:
    # static fields (attribute)
    co = 0
    # Constructure
    def __init__(self):
        # attribute
        self.DB = {}

    # Method (Function)
    def PrintTasks(self):
        for item in self.DB:
            print(item)

if __name__ == "__main__":

    instance  = TodoList()
    instance2 = TodoList()

    instance.DB["key"] = "value"

    TodoList.co= 10
    print(instance.co)
    print(instance2.co)
# instance2.DB