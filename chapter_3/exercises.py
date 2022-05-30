import sys

class DN:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next 
        self.prev = prev
        

class DLL:
    def __init__(self):
        self.head = DN()
        self.tail = DN()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

class SN:
    def __init__(self, data=None):
        self.data = data
        self.ref = None

class SLL:
    def __init__(self):
        self.head = None


#------------------------------------------------------------------------------#
#Question 1
"""
The section “Adding Cells at the End” gives an O(N) algorithm for adding an item
at the end of a singly linked list. If you keep another variable, bottom, that
points to the last cell in the list, then you can add items to the end of the
list in O(1) time. Write such an algorithm. How does this complicate other
algorithms that add an item at the beginning or end of the list, find an 
item, and remove an item? Write an algorithm for removing an item from this
kind of list.
"""

def delete_after(after_me, bottom):
    # The problem comes with changing the bottom if it's being deleted
    if after_me is None:
        bottom = after_me
    
    # All else is normal:
    after_me.next = after_me.next.next

    return bottom

#------------------------------------------------------------------------------#
# Question 2
'''
Write an algorithm to find the largest item in an unsorted singly linked
list with cells containing integers.
'''

def find_largest(self):
    largest = sys.minint
    n = self.head
    while n.next is not None:
        if n.data > largest:
            largest = n.data
        n = n.next
    
    return largest

#------------------------------------------------------------------------------#

# Question 3
'''
Write an algorithm to add an item at the top of a doubly linked list.
'''

# already done

#------------------------------------------------------------------------------#

# Question 4
'''
Write an algorithm to add an item at the bottom of a doubly linked list.
'''

# already done

#------------------------------------------------------------------------------#

# Question 5
'''
If you compare the algorithms you wrote for Exercises 3 and 4 to the
InsertCell algorithm shown in the section “Doubly Linked Lists,” you
should notice that they look very similar. Rewrite the algorithms you wrote
for Exercises 3 and 4 so that they call the InsertCell algorithm instead of
updating the list’s links directly.
'''

# already done

#------------------------------------------------------------------------------#    

#------------------------------------------------------------------------------#    

# Question 6
'''
Write an algorithm that deletes a specifi ed cell from a doubly linked list.
Draw a picture that shows the process graphically.
'''

def delete_cell(target):
    # Update the next cell's prev link
    target.next.prev = target.prev

    # Update the previous cell's next link
    target.prev.next = target.next
    
#------------------------------------------------------------------------------#

