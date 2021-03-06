class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if self.head and self.head.next_node:
            previous = self.head
            current = self.head.next_node
            previous.next_node = None
            while current.next_node:
                prevprev = previous
                previous.next_node = prevprev
                previous = current
                current = current.next_node
                previous.next_node = prevprev
            self.head = current
            self.head.next_node = previous
        pass
