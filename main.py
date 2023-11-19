#push_back(val), pop_back(), insert(index, val), delete(index), search(val), resize(val, count), clear()
class dynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.arr = [None] * self.capacity


    def push_back(self, val):
        if self.size == self.capacity:
            self.capacity *= 2
            new_array = [None] * self.capacity
            for i in range(len(self.arr)):
                new_array[i] = self.arr[i]
            self.arr = new_array
        self.arr[self.size] = val
        self.size += 1

    def pop_back(self):
        self.arr[self.size - 1] = None

    def insert(self, index, val):
        if index > self.size or index < 0:
            raise IndexError
        elif index == self.size:
            self.push_back(val)
            return
        elif self.size == self.capacity:
            self.capacity *= 2
            new_array = [None] * self.capacity
            for i in range(self.size):
                new_array[i] = self.arr[i]
            self.arr = new_array

        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i - 1]
        self.arr[index] = val

    def delete(self, index):
        if index > self.size or index < 0:
            raise IndexError
        for i in range(index, self.size):
            try:
                self.arr[i] = self.arr[i + 1]
            except IndexError:
                self.arr[i] = None

    def search(self, val):
        for i in range(self.size):
            if self.arr[i] == val:
                return f'This value is under {i} index'
        return 'Value not found'

    def resize(self, val, count):

        if count > self.size:
            diff = count - self.size

            while count > self.capacity:
                self.capacity *= 2
                new_array = [None] * self.capacity
                for i in range(self.size):
                    new_array[i] = self.arr[i]
                self.arr = new_array
            for i in range(diff):
                self.arr[self.size] = val
                self.size += 1
        else:
            new_array = [None] * count
            for i in range(count):
                new_array[i] = self.arr[i]
            self.arr = new_array

    def clear(self):
        self.size = 0
        self.capacity = 1
        self.arr = [None] * self.capacity


arr = dynamicArray()
arr.push_back(1)
arr.push_back(2)
arr.push_back(3)
arr.push_back(4)
arr.push_back(5)
arr.push_back(6)
arr.push_back(7)
arr.resize(4, 15)
arr.clear()
print(arr.arr)