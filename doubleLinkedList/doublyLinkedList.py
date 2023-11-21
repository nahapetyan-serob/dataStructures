class DoublyLinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next_node = None
            self.prev_node = None
    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()

    def push_back(self, val):
        new_node = self.Node(val)

        if self.head.data is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

    def push_front(self, val):
        new_node = self.Node(val)

        if self.head.data is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node


    def pop_back(self):
        if self.head.data is None:
            return 'Empty list, nothing to pop'
        else:
            val = self.tail
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            return val


    def pop_front(self):

        if self.head.data is None:
            print('There are no nodes to pop')
        else:
            val = self.head
            self.head = self.head.next_node
            self.head.prev_node = None
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
            while current_position < position and current is not None:
                current = current.next_node
                current_position += 1
            if current_position == position:
                if current.next_node is None:
                    self.push_back(val)
                else:
                    new_node.next_node = current.next_node
                    current.next_node.prev_node = new_node
                    current.next_node = new_node
                    new_node.prev_node = current
            else:
                raise IndexError

    def delete(self, position):
        if self.head is None:
            print('Nothing to delete, empty list')
        elif self.head.next_node is None and position == 0:
            self.head = None
            self.tail = None
        else:
            current_position = 1
            current = self.head
            while current_position < position and current.next_node is not None:
                current_position += 1
                current = current.next_node
            if current_position == position:
                if current.next_node is None:
                    self.tail = self.tail.prev_node
                    self.tail.next_node = None
                else:
                    current.prev_node.next_node = current.next_node
                    current.next_node.prev_node = current.prev_node
                    current.next_node = None
                    current.prev_node = None
            else:
                raise IndexError

    def insert_ddl(self, other, position):
        if not isinstance(other, DoublyLinkedList):
            print('Not a SingleLinkedList instance')
        elif self.head is None or other.head is None:
            print('One of the lists is empty')
        elif position == 0:
            other.tail.next_node = self.head
            self.head.prev_node = other.tail
            other.tail = None
            self.head = other.head
            other.head = None
        else:
            current = self.head
            current_position = 0
            while current_position < position and current is not None:
                current = current.next_node
                current_position += 1
            if current_position == position:
                if current.next_node is None:
                    current.next_node = other.head
                    other.head.prev_node = current
                    self.tail = other.tail
                    other.tail = None
                    other.head = None
                else:
                    current.next_node.prev_node = other.tail
                    other.tail.next_node = current.next_node
                    other.tail = None
                    other.head.prev_node = current
                    current.next_node = other.head
                    other.head = None

    def reverse(self):
        if self.head is None:
            print('Nothing to reverse, empty list')
        elif self.head.next_node is None:
            print('Nothing to reverse, list has only one node')
        else:
            current = self.head
            prev = None
            while current is not None:
                current.prev_node = current.next_node
                current.next_node = prev

                prev = current
                current = current.prev_node
            self.head = prev
            self.tail = self.head

    def getMiddleNode(self):
        fast = self.head
        slow = self.head
        #Empty linked list
        if self.head is None:
            return 'No element in the list'
        #Linked list with one element, return that element
        elif self.head.next_node is None:
            return self.head.data
        else:
            while fast is not None and fast.next_node is not None:
                fast = fast.next_node.next_node
                slow = slow.next_node
            return slow.data

    def hasCycle(self):
        fast = self.head
        slow = self.head

        while fast is not None and fast.next_node is not None:
            slow = slow.next_node
            fast = fast.next_node.next_node
            if fast is slow:
                return True
        return False


    def getStartPoint(self):
        if not self.hasCycle():
            return 'This list does not have a cycle'
        seen = set()
        current = self.head
        while current not in seen:
            seen.add(current)
            current = current.next_node
        return current

    def mergeTwoSortedLists(self, other):
        if not isinstance(other, DoublyLinkedList):
            raise ValueError('Can not merge')
        i = self.head
        j = other.head
        new_list = DoublyLinkedList()
        current = new_list.head
        while i is not None and j is not None:
            if i.data <= j.data:
                current.next_node = i
                i.prev_node = current
                i = i.next_node
            else:
                current.next_node = j
                j.prev_node = current
                j = j.next_node
            current = current.next_node

        while i is not None:
            current.next_node = i
            i.prev_node = current
            i = i.next_node
            current = current.next_node

        while j is not None:
            current.next_node = j
            j.prev_node = current
            j = j.next_node
            current = current.next_node

        new_list.head = new_list.head.next_node
        new_list.tail = current

        return new_list