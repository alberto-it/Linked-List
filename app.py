def lb():
    print('_' * 65)
    print()

print('\n* * * * * * * * * * * *\n* Singly Linked List  * \n* * * * * * * * * * * *\n')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self): self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None: self.head = new_node
        else:
            current = self.head
            while current.next: current = current.next #Loop to the end
            current.next = new_node

    def delete(self, data):
        if self.head is None:
            print('List is empty, nothing to remove')
            return
        current = self.head
        if current.data == data:
            self.head = current.next
            return
        previous = None
        while current:
            if current.data == data:
                previous.next = current.next
                return
            previous = current
            current = current.next
        print(f"{data} is not in this Singly Linked List.")

    def print_list(self):
        print('Head\n ↳ ', end="")
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")


nums = SinglyLinkedList()

print("Inserting 5... ", end="")
nums.insert_at_beginning(5)
print("Inserting 3 in front... ", end="")
nums.insert_at_beginning(3)
print("Inserting 1 in front... ")
nums.insert_at_beginning(1)
print("\nList after insertions:")
nums.print_list()
lb()
print("Inserting 7 in the back... ", end="")
nums.insert_at_end(7)
print("Inserting 9 in the back...")
nums.insert_at_end(9)
print("\nList after insertions:")
nums.print_list()
lb()
print("Deleting 3...")
nums.delete(3)
print("\nList after deletion:")
nums.print_list()
lb()

print('\n* * * * * * * * * * * *\n* Doubly Linked List  * \n* * * * * * * * * * * *\n')
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = DNode(data)
        if self.head is None: self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = DNode(data)
        if self.head is None: self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, data):
        if self.head is None: print('List is empty, nothing to remove')
        else:
            if self.head.data == data:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                return
            current = self.head
            while current:
                if current.data == data:   
                    if current.prev: current.prev.next = current.next
                    if current.next: current.next.prev = current.prev
                    return
                current = current.next
            print(f"{data} is not in this Doubly Linked List.")
                
    def print_forward(self):
        current = self.head
        while current.next:
            print(current.data, end=" <-> ")
            current = current.next
        print(current.data)

    def print_backward(self):
        current = self.tail
        while current.prev:
            print(current.data, end=" <-> ")
            current = current.prev
        print(current.data) 

nums = DoublyLinkedList()
print("Inserting 5...", end=" ")
nums.insert_at_beginning(5)
print("Inserting 3 in front...", end=" ")
nums.insert_at_beginning(3)
print("Inserting 1 in front...")
nums.insert_at_beginning(1)
print("\nForward list after insertion:")
nums.print_forward()
print("\nBackward list after insertion:")
nums.print_backward()
lb()
print("Inserting 7 in the back...")
nums.insert_at_end(7)
print("Inserting 9 in the back...")
nums.insert_at_end(9)
print("\nForward list after insertion:")
nums.print_forward()
lb()
print("Deleting 3...")
nums.delete(3)
print("\nForward list after deletion:")
nums.print_forward()
print("\nBackward list after deletion:")
nums.print_backward()
lb()