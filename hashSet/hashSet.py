class MyHashSet:

    def __init__(self):
        self.table_size = 13
        self.table = [[] for _ in range(self.table_size)]
        self.elem_count = 0
        self.load_factor = self.elem_count / self.table_size

    def hash_function(self, elem: int) -> int:
        hash_value = 31
        hash_value ^= elem
        return hash_value % self.table_size

    @staticmethod
    def find_next_table_size(self) -> None:

        def is_prime(number: int) -> bool:
            if number < 2:
                return False
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    return False
            return True

        self.table_size *= 2
        while True:
            if is_prime(self.table_size):
                return
            self.table_size += 1

    def rehash(self) -> None:
        old_table = [i for i in self.table]
        self.table = [[] for _ in range(self.table_size)]
        for row in old_table:
            for element in row:
                self.add(element)

    def add(self, key: int) -> None:
        index = self.hash_function(key)
        if not self.table[index]:
            self.table[index] = []
        self.table[index].append(key)
        self.elem_count += 1
        if self.load_factor > 0.75:
            self.rehash()

    def remove(self, key: int) -> None:
        index = self.hash_function(key)
        if self.table[index]:
            self.table[index] = [i for i in self.table[index] if i != key]
        self.elem_count -= 1

    def contains(self, key: int) -> bool:
        index = self.hash_function(key)
        if self.table[index]:
            for i in self.table[index]:
                if i == key:
                    return True
        return False
