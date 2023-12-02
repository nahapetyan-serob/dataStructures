class Soll:
    class Node:
        def __init__(self, val = 0):
            self.val = val
            self.next_node = None
            self.prev_node = None
            self.asc = None
            self.desc = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.ascHead = None
        self.descHead = None

    def put_in_sorted_order(self, node):
        if self.ascHead is None:
            self.ascHead = node
            self.descHead = node
        elif self.ascHead.val > node.val:
            node.asc = self.ascHead
            self.ascHead.desc = node
            self.ascHead = node
        elif self.descHead.val < node.val:
            self.descHead.asc = node
            node.desc = self.descHead
            self.descHead = node
        else:
            curr = self.ascHead
            while curr.asc is not None and curr.asc.val < node.val:
                curr = curr.asc

            node.asc = curr.asc
            curr.asc.desc = node
            curr.asc = node
            node.desc = curr

    def remove_from_sorted_order(self, node):
        if self.ascHead is node:
            removing = self.ascHead
            self.ascHead = self.ascHead.asc
            self.ascHead.desc = None
            removing.asc = None
        elif self.descHead is node:
            removing = self.descHead
            self.descHead = self.descHead.desc
            self.descHead.asc = None
            removing.desc = None
        else:
            node.asc.desc = node.desc
            node.desc.asc = node.asc
            node.asc = None
            node.desc = None




    def push_back(self, val):
        new_node = self.Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.put_in_sorted_order(new_node)
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node
            self.put_in_sorted_order(new_node)


    def push_front(self, val):
        new_node = self.Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.put_in_sorted_order(new_node)

        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node
            self.put_in_sorted_order(new_node)

    def pop_back(self):
        if self.head is None:
            return 'Empty list, nothing to pop'
        else:
            self.remove_from_sorted_order(self.tail)
            val = self.tail
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            return val

    def pop_front(self):

        if self.head is None:
            print('There are no nodes to pop')
        else:
            self.remove_from_sorted_order(self.head)
            val = self.head
            self.head = self.head.next_node
            self.head.prev_node = None
            return val

    def search(self, val):
        if self.head is None:
            return 'Linked list is empty'
        elif self.head.next_node is None:
            if self.head.val == val:
                return 0
        current = self.head
        position = 1
        while current.next_node is not None:
            if current.next_node.val == val:
                return position
            current = current.next_node
            position += 1
        return 'Not found'

    def insert(self, position, val):
        new_node = self.Node(val)

        if position == 0:
            new_node.next_node = self.head
            self.head = new_node
            self.put_in_sorted_order(new_node)
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
                    self.put_in_sorted_order(new_node)
            else:
                raise IndexError

    def delete(self, position):
        if self.head is None:
            print('Nothing to delete, empty list')
        elif self.head.next_node is None and position == 0:
            self.head = None
            self.tail = None
            self.ascHead = None
            self.descHead = None
        elif position == 0:
            self.remove_from_sorted_order(self.head)
            self.head = self.head.next_node
            self.head.prev_node.prev_node = None
            self.head.prev_node.next_node = None
            self.head.prev_node = None

        else:
            current_position = 0
            current = self.head
            while current_position < position and current.next_node is not None:
                current_position += 1
                current = current.next_node
            if current_position == position:
                if current.next_node is None:
                    self.remove_from_sorted_order(self.tail)
                    self.tail = self.tail.prev_node
                    self.tail.next_node = None

                else:
                    self.remove_from_sorted_order(current)
                    current.prev_node.next_node = current.next_node
                    current.next_node.prev_node = current.prev_node
                    current.next_node = None
                    current.prev_node = None
            else:
                raise IndexError

    def insert_soll(self, other, position):
        if not isinstance(other, Soll):
            print('Not a Soll instance')
            return
        elif self.head is None or other.head is None:
            print('One of the lists is empty')
            return
        curr = other.head
        while curr is not None:
            self.put_in_sorted_order(curr)
            curr = curr.next_node
        if position == 0:
            other.tail.next_node = self.head
            self.head.prev_node = other.tail
            other.tail = None
            self.head = other.head
            other.head = None

        else:
            current = self.head
            current_position = 1
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
        # Empty linked list
        if self.head is None:
            return 'No element in the list'
        # Linked list with one element, return that element
        elif self.head.next_node is None:
            return self.head.data
        else:
            while fast is not None and fast.next_node is not None:
                fast = fast.next_node.next_node
                slow = slow.next_node
            return slow.data

    def hasCycle(self):
        if self.head is None:
            return False
        fast = self.head
        slow = self.head

        while fast is not None and fast.next_node is not None:
            slow = slow.next_node
            fast = fast.next_node.next_node
            if fast is slow:
                return True
        return False

    def getStartPoint(self):
        if self.head is None:
            return 'There is no cycle'
        fast = self.head
        slow = self.head

        while fast is not None and fast.next_node is not None:
            slow = slow.next_node
            fast = fast.next_node.next_node
            if fast is slow:
                slow = self.head
                while slow is not fast:
                    slow = slow.next_node
                    fast = fast.next_node
                return slow


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

    def print_start_to_end(self):
        if self.head is None:
            print('Empty list')
        else:
            current = self.head
            while current is not None:
                print(current.val, end=',')
                current = current.next_node
        print('\n')

    def print_end_to_start(self):
        if self.head is None:
            print('Empty list')
        else:
            current = self.tail
            while current is not None:
                print(current.val, end=',')
                current = current.prev_node
        print('\n')

    def print_in_ascending_order(self):
        if self.head is None:
            print('Empty list')
        else:
            current = self.ascHead
            while current is not None:
                print(current.val, end=',')
                current = current.asc
        print('\n')

    def print_in_descending_order(self):
        if self.head is None:
            print('Empty list')
        else:
            current = self.descHead
            while current is not None:
                print(current.val, end = ',')
                current = current.desc
        print('\n')

soll = Soll()
soll.push_back(6)
soll.push_back(5)
soll.push_front(3)
soll.insert(1, 7)
soll.delete(0)
a = Soll()
a.push_front(1)
a.push_front(2)
a.push_front(3)
soll.insert_soll(a, 2)
print('start to end')
soll.print_start_to_end()
print('end to start')
soll.print_end_to_start()
print('ascending')
soll.print_in_ascending_order()
print('descending')
soll.print_in_descending_order()
