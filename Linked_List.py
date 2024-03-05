class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        init = Node('init')
        self.head = init
        self.tail = init

        self.current_node = None
        self.data_num = 0

    def __len__(self):
        return self.data_num

    def __str__(self):
        current_node = self.head
        current_node = current_node.next
        s = ''
        for i in range(self.data_num):
            s += f'{current_node.data},  '
            current_node = current_node.next
        return s[:-3]

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.data_num += 1

    def pop(self):
        last_value = self.tail.data
        current_node = self.head

        for i in range(self.data_num):
            if current_node.next is self.tail:
                self.tail = current_node
                break
            current_node = current_node.next

        self.data_num -= 1
        return last_value

    def find(self, data):
        idx = -1
        current_node = self.head

        for i in range(self.data_num+1):
            if current_node.data == data:
                return idx
            idx += 1
            current_node = current_node.next

        return -1


l = LinkedList()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l.append(15)

print(l.head.data)
print(l.head.next.data)
print(l.head.next.next.data)
print(l.head.next.next.next.data)

print(len(l))

print(str(l))