class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    def remove_from_front(self):
        # remove first item and return value
        current_head = self.head
        new_head = current_head.next
        self.head = new_head
        return current_head.value
    def remove_from_back(self):
        # remove last node and return value
        runner = self.head
        while runner.next.next != None:
            runner = runner.next
        current_end = runner.next
        runner.next = None
        return current_end.value
    def remove_val(self, val):
        # remove first node with given value
        runner = self.head
        # print(runner.value)
        if runner.value == val:
            self.head = runner.next
            return self
        else:
            while runner.next != None:
                if runner.next.value == val:
                    runner.next = runner.next.next
                    return self
                runner = runner.next
            print("Value not found!")
            return self
    def insert_value(self, val, n=1):
        # insert value at nth node
        if n == 1:
            self.add_to_front(val)
            return self
        else:
            runner = self.head
            for i in range(1, n-1):
                runner = runner.next
            if runner.next == None:
                self.add_to_back(val)
            else:
                new_node = SLNode(val)
                pushed_node = runner.next
                runner.next = new_node
                new_node.next = pushed_node
            return self

my_list = SLList()
my_list.add_to_front("are").add_to_front("Linked lists"). add_to_back("fun!").print_values()