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

        if self.head.data is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def pop_back(self):
        if self.head.data is None:
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
        if self.head.data is None:
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
        if self.head.data is None:
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

    def reverse(self):
        prev = self.Node()
        _next = self.Node()
        current = self.head

        while current is not None:
            _next = current.next_node
            current.next_node = prev

            prev = current
            current = _next
        self.head = prev

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
        if not isinstance(other, SingleLinkedList):
            return "Can't merge!"
        new_sll = SingleLinkedList()
        current = new_sll.head
        i = self.head
        j = other.head
        while i is not None and j is not None:
            if i.data <= j.data:
                current.next_node = i
                i = i.next_node
            else:
                current.next_node = j
                j = j.next_node
            current = current.next_node

        while i is not None:
            current.next_node = i
            i = i.next_node
            current = current.next_node

        while j is not None:
            current.next_node = j
            j = j.next_node
            current = current.next_node
        new_sll.head = new_sll.head.next_node
        return new_sll

    def __reverse_recursive(self, node):
        if not node or not node.next_node:
            return node
        tmp = self.__reverse_recursive(node.next_node)
        node.next_node.next_node = node
        node.next_node = None
        return tmp

    def reverse_recursive(self):
        self.head = self.__reverse_recursive(self.head)









a = SingleLinkedList()
b = SingleLinkedList()
a.push_front(2)
#c = a.mergeTwoSortedLists(b)
print(a.head.data)