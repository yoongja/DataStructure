import os
from midterm import *

if __name__ == '__main__':
    q = CircularQueue()
   

    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(7)
    q.enqueue(9)
    print(q)
 

    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(q)
 

    q.enqueue(2)
    q.enqueue(4)
    print(q)