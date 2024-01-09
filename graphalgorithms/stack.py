class Stack():
    def __init__(self) -> list:
        self.stack_list=list()
    
    def add(self, value):
        self.append(value)
    
    def pop(self):
        self.pop()
    
    def empty(self):
        self.clear()
    
    def top(self):
        return self[-1]
    