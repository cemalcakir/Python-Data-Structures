class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self, length):
        self.length = length
        self.map = [None] * self.length

    def put(self, key: int, value: int) -> None:
        "Inserting an element to hashmap."
        index = key % self.length
        if self.map[index]:
            current = self.map[index]
            if current.key == key:
                current.value = value
                return
            while current.next:
                if current.next.key == key:
                    current.next.value = value
                    return
                current = current.next
            current.next = ListNode(key, value)
        else:
            self.map[index] = ListNode(key, value)

    def get(self, key: int) -> int:
        "Getting the value of given key."
        index = key % self.length
        current = self.map[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        "Remove given key and value from hashmap."
        index = key % self.length
        current = self.map[index]
        if current:
            if current.key == key:
                self.map[index] = current.next
            else:
                while current.next:
                    if current.next.key == key:
                        current.next = current.next.next
                        return
                    current = current.next
