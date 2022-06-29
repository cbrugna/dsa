# Implement a singly linked list 

class Node:
    def __init__(self, data=None):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        node = Node(data)
        node.ref = self.head
        self.head = node


    def push_back(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = node

    def insert_after(self, data, after):
        node = Node(data)
        if self.head is None:
            print("List is empty.")
            return
        else:
            n = self.head
            while n.data is not after:
                n = n.ref
            node.ref = n.ref
            n.ref = node

    def delete(self, delete):
        if self.head is None:
            print("List is empty")
            return
        if delete is self.head.data:
            self.head = self.head.ref
            return

        n = self.head
        while n.ref is not None:
            if delete is n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node to delete is not present.")
        else:
            n.ref = n.ref.ref

    def print_list(self):
        if self.head is None:
            print("List is empty.")
        else:
            print_str = ""
            while(self.head is not None):
                print_str += str(self.head.data) + "-->"
                self.head = self.head.ref
            print(print_str)
        




if __name__ == '__main__':
    ll = LinkedList()
    ll.push_back(3)
    ll.push_front(2)
    ll.push_back(11)
    ll.push_back(8)
    ll.insert_after(88, 8)
    ll.delete(2)
    ll.print_list()


    

    




    