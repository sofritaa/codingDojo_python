class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        new_node = SLNode(val)
        if not self.head:
            self.head = new_node
        else:
            runner = self.head
            while runner.next:
                runner = runner.next
            runner.next = new_node
        return self

    def remove_from_front(self):
        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        return removed_value

    def remove_from_back(self):
        if not self.head:
            return None
        elif not self.head.next:
            return self.remove_from_front()
        else:
            runner = self.head
            while runner.next.next:
                runner = runner.next
            removed_value = runner.next.value
            runner.next = None
            return removed_value

    def remove_val(self, val):
        if not self.head:
            return None
        elif self.head.value == val:
            return self.remove_from_front()
        else:
            runner = self.head
            while runner.next and runner.next.value != val:
                runner = runner.next
            if not runner.next:
                return None
            removed_value = runner.next.value
            runner.next = runner.next.next
            return removed_value

    def insert_at(self, val, n):
        if n == 0:
            return self.add_to_front(val)
        else:
            new_node = SLNode(val)
            runner = self.head
            for _ in range(n-1):
                if not runner:
                    return None
                runner = runner.next
            if not runner:
                return None
            new_node.next = runner.next
            runner.next = new_node
        return self

my_list = SList()
my_list.add_to_front("C").add_to_front("B").add_to_front("A")
my_list.add_to_back("D").add_to_back("E")

my_list.print_values()


print(my_list.remove_from_front())  
print(my_list.remove_from_back())   

my_list.print_values()

print(my_list.remove_val("C"))   
my_list.print_values()


my_list.insert_at("X", 0)
my_list.insert_at("Y", 2)

my_list.print_values()
