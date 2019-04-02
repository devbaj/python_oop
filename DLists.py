class DLNode:
    def __init__(self, val):
        self.prev = None
        self.value = val
        self.next = None

class DList:
    def __init__(self):
        self.head = None
    def add_to_end(self, val):
        new_node = DLNode(val)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node
        new_node.prev = runner
        return self
    def delete_node(self, n):
        for i in range(1, n-1):
            runner = runner.next
        if runner.next == None:
            runner.prev.next = None
        else:
            runner.next.prev = runner.prev
            runner.prev.next = runner.next
        return self
    def insert_node(self, val, n):
        runner = self.head
        for i in range(1, n-1):
            runner = runner.next
        if runner.next == None:
            self.add_to_end(val)
        else:
            new_node = DLNode(val)
            new_node.prev = runner
            new_node.next = runner.next
            runner.next.prev = new_node
            runner.next = new_node
        return self
    def print_list(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self