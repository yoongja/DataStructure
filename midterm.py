class CircularQueue():
    def __init__(self, size=None):
        if size == None:
            size = 5
            self.max_que = size + 1         
        else:
            self.max_que = size + 1
        self.items = [0] * (self.max_que)
        self.front = self.max_que-1
        self.rear = self.max_que-1
 

    def make_empty(self):
        self.items = [ ]
        self.front = self.max_que-1
        self.rear = self.max_que-1
   

    def is_empty(self):
        return (self.rear == self.front)
 

    def is_full(self):
        return ((self.rear + 1) % self.max_que == self.front)
   

    def enqueue(self, newItem):
        if self.is_full():
            print("Queue is Full")
        else:
            self.rear = (self.rear + 1) % self.max_que
            self.items[self.rear] = newItem
 

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            self.front = (self.front + 1) % self.max_que
            return self.items[self.front]
 

def __str__(self):
        print_items = []
        if self.front<self.rear:
            for idx in range(self.front + 1,self.rear):
                print_items.append(self.items[idx])
        else:
            for idx in range((self.front +1)%size,self.rear):
                print_items.append(self.items[idx])
            for idx in range(______[d]_____):
                print_items.append(self.items[idx])
        return str(print_items).replace(',', ' ')