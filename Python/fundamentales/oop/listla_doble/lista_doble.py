class DListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add_to_end(self, value):
        new_node = DListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                break
            current = current.next

    def insert_before(self, value, target):
        new_node = DListNode(value)
        current = self.head
        while current:
            if current.value == target:
                if current.prev:
                    current.prev.next = new_node
                    new_node.prev = current.prev
                else:
                    self.head = new_node
                new_node.next = current
                current.prev = new_node
                break
            current = current.next

    def print_values(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


my_list = DLinkedList()
my_list.add_to_end("A")
my_list.add_to_end("B")
my_list.add_to_end("C")

my_list.print_values()

my_list.remove("B")

my_list.print_values()

my_list.insert_before("X", "C")

my_list.print_values()
