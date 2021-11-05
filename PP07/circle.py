class NodeType:
    """ Node Type """
    def __init__(self, item):
        self.info = item
        self.next = None

class CircularLL:
    def __init__(self):
        self.listData = None
        self.length = 0
        self.currentPos = None

    def is_full(self):
        try:
            location = NodeType("test")
            return False
        except:
            return True

    def length_is(self):
        return self.length

    def make_empty(self):
        while self.listData != None:
            tempPtr = self.listData.next
            del self.listData
            self.listData = tempPtr
        self.length = 0

    def find_item(self, listData, item):

        moreToSearch = True
        location = self.listData
        predLoc = self.listData
        found = False
        
        while(moreToSearch and not found):
            if(item < int(location.info)):
                moreToSearch = False
            elif item == location.info:
                found = True
            else:
                predLoc = location
                location = location.next 
                moreToSearch = (location != self.listData.next)
        return location,predLoc

    def insert_item(self, item):
        newnode = NodeType(item)
        if self.listData != None:
            location,predLoc = self.find_item(self.listData,item)
            newnode.next = predLoc.next
            predLoc.next = newnode

            if self.listData.info < item :
                self.listData= newnode
        else:
            self.listData = newnode
            newnode.next = newnode
        self.length += 1
        


    def delete_item(self, item):

        location = NodeType("")
        predLoc = NodeType("")

        self.find_item(self.listData,item)
        if predLoc == location:
            self.listData = None
        else:
            predLoc.next = location.next
            if location == self.listData:
                self.listData= predLoc
            location = None
            self.length -= 1
   

    def reset_list(self):
        self.currentPos = None

    def get_next_item(self):
        if self.currentPos == None:
            self.currentPos = self.listData
        else:
            self.currentPos = self.currentPos.next
        return self.currentPos.info

    def __str__(self):
        self.reset_list()
        items = []
        for i in range(0, self.length):
            t = self.get_next_item()
            items.append(str(t))
        return " ".join(items)
