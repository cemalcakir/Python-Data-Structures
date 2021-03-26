class Node:
    "Single node of a singly linked list"

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        "Insertion method"
        if (self.head):
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
        else:
            self.head = Node(data)

    def delete(self, data):
        "Delete an element from linked list"
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current:
                if current.next.data == data:
                    current.next = current.next.next
                    return
                current = current.next

    def __str__(self):
        "Prints linked list object as an array"
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        return str(arr)
