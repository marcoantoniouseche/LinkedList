class Node:
    def __init__(self, value, link=None):
        self.value = value
        self.link = link

    def getValue(self):
        return self.value

    def getLink(self):
        return self.link

    def setValue(self, value):
        self.value = value

    def setLink(self, link):
        self.link = link

class LinkedList:
    def __init__(self, value=None):
        self.node = Node(value)
        self.head_node = self.node

    def add_value(self, value):
        new_node = Node(value)
        current_node = self.node
        current_node.setLink(new_node)
        self.node = new_node
        
    def printll(self): #ll mean 'Linked list'
        current_node = self.head_node
        printout = '[ '
        while current_node:
            printout += str(current_node.getValue()) + ', '
            current_node = current_node.getLink()
        printout += ']'
        print(printout)
        
    def delete_value(self, value):
        current_node = self.head_node
        if current_node.getValue() == value:
            self.head_node = current_node.getLink()
            current_node.setLink(None)
        else:
            next_node = current_node.getLink()
            while next_node:
                if next_node.getValue() == value:
                    current_node.setLink(next_node.getLink())
                    next_node.setLink(None)
                    next_node = None
                else:
                    current_node = next_node
                    next_node = next_node.getLink()
        
objec = LinkedList(4)
objec.add_value(5)
objec.add_value(6)
objec.add_value(7)
objec.printll()
objec.delete_value(6)
objec.printll()