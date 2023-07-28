

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
            return
        else:
            current = self.tail
            current.next = node
            current.next.prev = current
            self.tail = node

            return

    def prepend(self, value):
        node = Node(value)
        
        if self.head == None:
            self.head = node
            return

        else:
            temp = self.head
            self.head = node
            self.head.next = temp
            return

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def search(self, value):

        if self.head == None:
            return False
        
        if self.head.value == value:
            return self.head 

        current = self.head
        while current.next:
            if current.value == value:
                return current
            current = current.next

        return False



if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.prepend(5)

    linked_list.display()  # Output: 5 -> 10 -> 20 -> 30

    linked_list.search(20)
    linked_list.search(29)
    # linked_list.delete(20)
    # linked_list.delete(5)
    # linked_list.display()  # Output: 5 -> 10 -> 30

    # print(linked_list.search(10))  # Output: True
    # print(linked_list.search(20))  # Output: False
