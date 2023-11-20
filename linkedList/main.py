#push_back(val), push_front(val), pop_back(), pop_front(), search(val)
#insert(position, val), delete(pos), insert(pos, singly_linked_list)
#reverse(head), getMiddleNode(head), hasCycle(head), getStartPoint(head), mergeTwoSortedLists

class SingleLinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next_node = None
    def __init__(self):
        self.head = self.Node()

    def push_back(self, val):
        new_node = self.Node(val)

        current = self.head
        if current.data is None:
            self.head = new_node
        else:
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_node


    def push_front(self, val):
        new_node = self.Node(val)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def pop_back(self):
        if self.head is None:
            print('There are no nodes to pop')
        elif self.head.next_node is None:
            val = self.head.data
            self.head = None
            return val
        else:
            current = self.head
            while current.next_node.next_node is not None:
                current = current.next_node
            val = current.next_node.data
            current.next_node = None
            return val

    def pop_front(self):
        if self.head is None:
            print('There are no nodes to pop')
        elif self.head.next_node is None:
            val = self.head.data
            self.head = None
            return val
        else:
            val = self.head.data
            self.head = self.head.next_node
            return val

    def search(self, val):
        if self.head is None:
            return 'Linked list is empty'
        elif self.head.next_node is None:
            if self.head.data == val:
                return 0
        current = self.head
        position = 1
        while current.next_node is not None:
            if current.next_node.data == val:
                return position
            current = current.next_node
            position += 1
        return 'Not found'

    def insert(self, position, val):
        new_node = self.Node(val)

        if position == 0:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            current_position = 1
            while current_position < position and current.next_node is not None:
                current = current.next_node
                current_position += 1
            if current_position == position:
                new_node.next_node = current.next_node
                current.next_node = new_node
            else:
                print('Position error')

    def delete(self, position):
        if self.head is None:
            print('Nothing to delete, empty list')
        elif position == 0 and self.head.next_node is not None:
            need_to_delete = self.head
            self.head = self.head.next_node
            del need_to_delete
        else:
            current_position = 1
            current = self.head
            while current_position < position and current.next_node is not None:
                current = current.next_node
                current_position += 1
            if current_position == position:
                need_to_delete = current.next_node
                current.next_node = current.next_node.next_node
                del need_to_delete
            else:
                print('Position error')

    def insert_ssl(self, other, position):
        if not isinstance(other, SingleLinkedList):
            print('Not a SingleLinkedList instance')
        elif self.head is None or other.head is None:
            print('One of the lists is empty')
        elif position == 0:
            other_current = other.head
            while other_current.next_node is not None:
                other_current = other_current.next_node
            other_current.next_node = self.head
            self.head = other.head
            other.head = None
        else:
            current = self.head
            current_position = 1
            while current_position < position and current.next_node is not None:
                current = current.next_node
                current_position += 1
            if current_position == position:
                other_current = other.head
                while other_current.next_node is not None:
                    other_current = other_current.next_node
                other_current.next_node = current.next_node
                current.next_node = other.head
                other.head = None
            else:
                print('Position error')

    def reverse(self, head):
        pass

    def getMiddleNode(self, head):
        pass

    def hasCycle(self, head):
        pass

    def getStartPoint(self, head):
        pass

    def mergeTwoSortedLists(self, head):
        pass




sll = SingleLinkedList()
b = SingleLinkedList()
b.push_back(111)
b.push_front(2232)
sll.push_back(5)
print(sll.head.data)
sll.push_front(10)
# sll.pop_back()
# sll.pop_front()
print(sll.search(25))
sll.insert(1,122)
sll.delete(1)
sll.insert_ssl(b, 1)
print(sll.head.data, sll.head.next_node.data, sll.head.next_node.next_node.data, sll.head.next_node.next_node.next_node.data)
