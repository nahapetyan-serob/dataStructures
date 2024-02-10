from typing import Union


class Heap:
    def __init__(self):
        self.arr = []
        self.heap_size = 0
        self.top = self.arr[0] if self.heap_size > 0 else None

    def get_right(self, i: int) -> int:
        if 2 * i + 2 < self.heap_size:
            return 2 * i + 2
        raise IndexError

    def get_left(self, i: int) -> int:
        if 2 * i + 1 < self.heap_size:
            return 2 * i + 1
        raise IndexError

    def swap(self, i, j) -> None:
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def max_heapify(self, index: int) -> None:
        if index == 0:
            return
        left = self.get_left(index)
        right = self.get_right(index)
        largest = index
        if left <= self.heap_size and self.arr[left] > self.arr[largest]:
            largest = left
        if right <= self.heap_size and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != index:
            self.swap(largest, index)
            self.max_heapify(largest)

    def build_max_heap(self) -> None:
        for i in range(self.heap_size // 2 - 1, -1, -1):
            self.max_heapify(i)

    def heap_sort(self) -> None:
        self.build_max_heap()
        for i in range(self.heap_size - 1, 0, -1):  # from the last element to second
            self.swap(0, self.heap_size - 1)
            self.heap_size -= 1
            self.max_heapify(0)

    def insert(self, value: int) -> None:
        self.arr.append(value)
        self.heap_size += 1
        i = self.heap_size - 1
        while i > 0 and self.arr[(i - 1) // 2] < self.arr[i]:
            self.swap((i - 1) // 2, i)
            i = (i - 1) // 2

    def extract_max(self) -> Union[int, str]:
        if self.heap_size < 1:
            return 'Empty heap'
        max_value = self.arr[0]
        self.swap(0, self.heap_size - 1)
        self.heap_size -= 1
        self.max_heapify(0)
        return max_value

    def increase_key(self, index: int, value) -> None:
        if index >= self.heap_size:
            raise IndexError(f"Choose between 0 and {self.heap_size - 1}")
        if self.arr[index] > value:
            raise ValueError(f"Given value must be higher than {self.arr[index]}")
        self.arr[index] = value
        i = index
        while i > 0 and self.arr[(i - 1) // 2] < self.arr[i]:
            self.swap((i - 1) // 2, i)
            i = (i - 1) // 2


heap = Heap()
heap.insert(5)
a = heap.extract_max()
print(a)
