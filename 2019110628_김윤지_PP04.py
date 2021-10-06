MAX_ITEMS = 100

class StackType:
    def __init__(self):
        self.info = []
        self.tp = -1

    def is_empty(self):
       
        if self.tp == -1 :
            return True
        else : 
            return False
        
    def is_full(self):
       
        if self.tp == MAX_ITEMS -1:
            return "True"
        else:
            return "False"
        
    def push(self, item):
       
        self.tp+=1
        self.info.append(item)
        
    def pop(self):
       
        self.tp-=1

    def top(self):
        
        if self.tp != -1 :
            return self.info[self.tp]
        else :
            return "Stack is Empty"
        