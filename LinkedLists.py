class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + " "
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    def count_values(self, value_to_count):
        count = 0
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() == value_to_count:
                count += 1
            current_node = current_node.get_next_node()
        return count

    def remove_node_all(self, value_to_remove):
        number_to_remove = self.count_values(value_to_remove)
        for i in range(number_to_remove):
            self.remove_node(value_to_remove)


ll = LinkedList(5)
for i in range(10, 21):
    ll.insert_beginning(i)
ll.insert_beginning(12)
ll.insert_beginning(12)

print(ll.stringify_list())

print(ll.remove_node_all(12))
print(ll.stringify_list())
