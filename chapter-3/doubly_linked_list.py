# Implement a doubly linked list 


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next 
        self.prev = prev
        

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        new_node.next.prev = new_node
        new_node.prev = self.head
        self.size += 1

    def push_back(self, data):
        new_node = Node(data)
        new_node.next = self.tail
        self.tail.prev.next = new_node
        new_node.next.prev = new_node
        new_node.prev = self.tail.prev
        self.size += 1
        
    def after_me(self, after_me, data):
        new_node = Node(data)
        n = self.head
        ctr = 0
        while n.next is not None and ctr != self.size+1:
            if n.data is after_me:
                print("asd")
                new_node.next = n.next #1
                new_node.prev = n #4
                n.next = new_node #2
                new_node.next.prev = new_node.next #3
                

                self.size+=1
            n = n.next
            ctr += 1
           

    def print(self):
        n = self.head
        ret = ''
        ctr = 0
        while n.next is not None:
            if ctr != 0 and ctr != self.size+1:
                if ctr == self.size:
                    ret += str(n.data)
                else:
                    ret += str(n.data) + "<->"
            n = n.next
            ctr += 1
        print(ret)

if __name__ == '__main__':
    dll = DLL()
    dll.push_front(8)
    dll.push_front(3)
    dll.push_back(11)
    dll.after_me(8, 28)
    dll.print()