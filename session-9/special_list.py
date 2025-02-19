class SpecialList: 
    def __init__(self):
        self.my_list = []

    def Add(self, item):
        self.my_list.insert(0, item)

    def Find(self, item):
        if item in self.my_list:
            return True
        return False

    def Access(self):
        if self.my_list == []:
            return 
        return self.my_list[0]

    def __add__(self, sp ):
        return self.my_list + sp.my_list

    def __len__(self):
        return len(self.my_list)

    def max(self):
        m:int = self.my_list[0]
        for i in range(1, len(self.my_list)):
            if self.my_list[i] > m:
                m= self.my_list[i]
        return m

    def min(self):
        m:int = self.my_list[0]
        for i in range(1, len(self.my_list)):
            if self.my_list[i] < m:
                m= self.my_list[i]
        return m
