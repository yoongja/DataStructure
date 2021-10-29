class NodeType:
    """ Node Type """
    def __init__(self, _name, _id):
        self.name = _name
        self.id = _id
        self.next = None

class SortedType:
    def __init__(self):
        self.listData = None
        self.length = 0
        self.currentPos = None

    def insert_item(self,person,number):
        location = self.listData
        predLoc = None
        moreToSearch = location != None
        while moreToSearch:
            if location.name < person:
                predLoc = location
                location = location.next
                moreToSearch = location != None
            elif location.name == person:
                if location.id < number:
                    predLoc = location
                    location = location.next
                    moreToSearch = location != None
                else:
                    moreToSearch = False
            else:
                moreToSearch = False

        newNode = NodeType(person,number)

        if predLoc == None:
            newNode.next = self.listData
            self.listData = newNode
        
        else : 
            newNode.next = location
            predLoc.next = newNode

        self.length += 1

    def length_is(self):
        return self.length

    def reset_list(self):
        self.currentPos = None

    def get_next_item(self):
        if self.currentPos == None:
            self.currentPos = self.listData
        name, id = self.currentPos.name, self.currentPos.id
        self.currentPos = self.currentPos.next

        return name, id

    def __str__(self):
        self.reset_list()
        items = []
        for i in range(0, self.length):
            name, id = self.get_next_item()
            items.append("(" +name + ", " + str(id) + ")\n")
        return "".join(items)
