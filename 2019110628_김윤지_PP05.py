MAX_ITEMS = 100

class QueueType():
    def __init__(self):
        self.info = []
        self.rear=MAX_ITEMS-1
        self.front=MAX_ITEMS-1

    def enqueue(self, data):
        self.rear = (self.rear+1) % MAX_ITEMS
        self.info.append(data)

    def dequeue(self):
        self.front = (self.front+1)%MAX_ITEMS
        return self.info[self.front]

    def is_empty(self):
        if (self.rear == self.front) :
            return "True"
        else:
            return "False"

    def is_full(self):
        if ((self.rear+1)%MAX_ITEMS==self.front) :
            return "True"
        else : 
            return "False"

    def make_empty(self):
        self.rear=MAX_ITEMS-1
        self.front=MAX_ITEMS-1