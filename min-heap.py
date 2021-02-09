class MinIntHeap:
    def __init__(self):
        self.items = []

    def get_left_child_index(self, parent_index):
        return parent_index * 2 + 1

    def get_right_child_index(self, parent_index):
        return parent_index * 2 + 2

    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def has_left_child(self, index):
        return self.get_left_child_index(index) < len(self.items)

    def has_right_child(self, index):
        return self.get_right_child_index(index) < len(self.items)

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def left_child(self, index):
        return self.items[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.items[self.get_right_child_index(index)]

    def parent(self, index):
        return self.items[self.get_parent_index(index)]

    def swap(self, index_one, index_two):
        self.items[index_one], self.items[index_two] = self.items[index_two], self.items[index_one]

    def __str__(self):
        return f"{self.items}"

    def peek(self):
        if not self.items:
            raise IndexError
        return self.items[0]

    def poll(self):
        if not self.items:
            raise IndexError
        item = self.items[0]
        self.items[0] = self.items.pop()
        self.heapify_down()
        return item

    def add(self, item):
        self.items.append(item)
        self.heapify_up()

    def heapify_up(self):
        index = len(self.items) - 1
        while self.has_parent(index) and self.parent(index) > self.items[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_right_child_index(index)

            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
            index = smaller_child_index


heap = MinIntHeap()
heap.add(5)
heap.add(10)
heap.add(15)
heap.add(11)
heap.add(1)
heap.add(0)
heap.add(12)
heap.add(12)
heap.add(9)
heap.add(12)
print(heap)
