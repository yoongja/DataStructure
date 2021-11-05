class NodeType:
    """ Node Type """
    def __init__(self, item):
        self.info = item
        self.next = None
        self.back = None

class DoublyLL:
    def __init__(self):
        self.head = NodeType('head')
    
    def find_item(self, item):
        
        moreToSearch = True
        location = self.head
        found = False
        
        while(moreToSearch and not found):
            if(item < location.info):
                moreToSearch = False
            elif item == location.info:
                found = True
            else:
                if location.next == None:
                    moreToSearch = False
                else:
                    location = location.next
        return location        
    
    def insert_item(self, item, new):
        newnode = NodeType(new)
        if self.head != None:
            location = self.find_item(item)
            if location.info>new :
                newnode.back = location.back
                newnode.next = location
                if location != self.head:
                    location.back.next = newnode
                else:
                    self.head = newnode
                location.back = newnode
            else:
                newnode.back = location
                location.next = newnode
                newnode.next = None
        else:
            self.head = newnode
            newnode.next = None
            newnode.back = None
            
    def delete_item(self, item):
        location = NodeType("")
        predLoc = NodeType("")

        self.find_item(item)
        if predLoc == location:
            self.head = None
        else:
            predLoc.next = location.next
            if location == self.head:
                self.head= predLoc
            location = None
            
    def __str__(self):
        cur_node = self.head
        items = []
        while cur_node is not None:
            items.append("(" + str(cur_node.info) + ")\n")
            cur_node = cur_node.next
        return "".join(items)

