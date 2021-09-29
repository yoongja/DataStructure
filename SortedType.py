from enum import Enum

MAX_ITEMS = 100

class Compare(Enum):
    LESS = 0
    GREATER = 1
    EQUAL = 2
    
class ItemType:
    """ Item Type """

    def __init__(self, val):
         self.value = val

    def compared_to(self, otherItem):
        if self.value<otherItem.value:
            return Compare.LESS
        elif self.value>otherItem.value:
            return Compare.GREATER
        return Compare.EQUAL 
    
    def __str__(self):
        return str(self.value)

class SortedType:
    """ Chapter 3: Sorted List """

    def __init__(self):
        self.length = 0
        self.info = []
        self.current_pos = -1

    def make_empty(self):
        self.length = 0

    def length_is(self):
        return self.length

    def is_full(self):
        if self.length == MAX_ITEMS:
            return True
        return False

    def insert_item(self, item):
        location = 0
        moreToSearch = (location < self.length)
        while moreToSearch :
            if item.compared_to(self.info[location]) == Compare.LESS :
                moreToSearch = False
            elif item.compared_to(self.info[location]) == Compare.GREATER:
                location+=1
                moreToSearch=(location<self.length)
        self.info.append(item)
        for i in range(self.length,location,-1):
            self.info[i] = self.info [i-1]
        self.info[location] = item
        self.length +=1
       
       
            
    def retrieve_item(self, item): # Binary Search
        first = 0
        last = self.length -1
        moreToSearch = (first <= last)
        found = False
        while moreToSearch and not found :
            midPoint = (first + last)//2
            if item.compared_to(self.info[midPoint]) == Compare.LESS :
                last = midPoint -1
                moreToSearch = (first<=last)
            elif item.compared_to(self.info[midPoint]) == Compare.GREATER:
                first = midPoint + 1
                moreToSearch = (first <= last )
            else :
                found=True
                item = self.info[midPoint]

    def delete_item(self, item):
        location = 0
        while item.compared_to(self.info[location]) != Compare.EQUAL:
            location+=1
        for i in range(location+1,self.length) :
            self.info[i-1] = self.info[i]
        self.length -=1

    def reset_list(self):
        self.current_pos = -1

    def get_next_item(self):
        self.current_pos += 1
        return self.info[self.current_pos]

    def __str__(self):
       self.reset_list()
        
       print_list = []
       for i in range(self.length):
         print_list.append(str(self.get_next_item()))
        
       return str(" ".join(print_list))