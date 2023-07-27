

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
        # if self.head is None:
        #     return True
        # return False
    
    def append(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
        
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    
    def prepend(self, value):
        node = Node(value)
        temp = self.head
        self.head = node
        node.next = temp
    
    def delete(self, value):
        if self.is_empty():
            return
        
        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                temp = current.next.next
                current.next = temp
                return
            current = current.next


    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.prepend(5)

    linked_list.display()  # Output: 5 -> 10 -> 20 -> 30

    linked_list.delete(20)
    linked_list.delete(5)
    linked_list.display()  # Output: 5 -> 10 -> 30

    print(linked_list.search(10))  # Output: True
    print(linked_list.search(20))  # Output: False