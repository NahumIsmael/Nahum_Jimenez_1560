from Node import Node

class LinkedList():
    

    def __init__(self):

        self.head = None
        

    def is_empty(self):

        return self.head == None
    

    def tail(self):

        curNode = self.head

        while (curNode.next != None):

            curNode = curNode.next

        return curNode
    

    def append(self, value):

        if (self.is_empty()):
            self.head = Node(value)
        else:
            self.tail().next = Node(value)
            

    def prepend(self, value):

        self.head = Node(value, self.head)
        

    def add_before(self, auxvalue, value):

        curNode = self.head

        while (curNode != None):

            if (curNode.data == auxvalue):

                if (curNode == self.head):
                    self.prepend(value)
                else:
                    curNode.data, curNode.next = value, Node(curNode.data, curNode.next)
                return

            curNode = curNode.next

        self.tail().next = Node(value)


    def add_after(self, auxvalue, value):

        curNode = self.head

        while (curNode.next != None):

            if (curNode.data == auxvalue):

                curNode.next = Node(value, curNode.next)
                return

            curNode = curNode.next

        self.tail().next = Node(value)

    
    def transversal(self):

        curNode = self.head

        while (curNode.next != None):

            print(curNode.data, "-> ", end="")
            curNode = curNode.next

        print(curNode.data)
        

    def remove(self, value):

        prevNode = None
        curNode = self.head

        while(curNode != None):

            if(curNode.data == value):

                if(prevNode == None):

                    self.head = self.head.next
                else:
                    prevNode.next = curNode.next
                return

            prevNode, curNode = curNode, curNode.next


    def pop(self):

        nodePop = None

        node = self.head

        while(node.next.next != None):

            node = node.next

        nodePop, node.next = node.next, None

        return nodePop


def main():
    
    Lista = LinkedList()
    print(f"¿Lista vacia? = {Lista.is_empty()}")
    Lista.append(5)
    Lista.append(6)
    Lista.append(7)
    Lista.remove(6)
    Lista.prepend(1)
    Lista.transversal()
    Lista.pop()
    Lista.transversal()
    
main()
