from typing import List


class DirectedGraph:

    def __init__(self, size: int) -> None:
        if size <= 0:
            raise ValueError("Size must be greater than 0.")
        self.size = size
        self.adjacency_list = [[] for _ in range(self.size)]

    def add_vertex(self) -> None:
        self.adjacency_list.append([])
        self.size += 1

    def remove_vertex(self, index: int) -> None:
        if 0 <= index < self.size:
            removing = self.adjacency_list.pop(index)
            for vertex in self.adjacency_list:
                if removing in vertex:
                    vertex.remove(removing)
            self.size -= 1
        else:
            raise IndexError(f"Invalid Index {index}")

    def add_edge(self, u: int, v: int) -> None:
        if u >= self.size or v >= self.size or u < 0 or v < 0:
            raise ValueError("Need to provide existing vertices")
        self.adjacency_list[u].append(v)
        #  self.adjacency_list[v].append(u)  # Uncomment to make the graph undirected

    def remove_edge(self, u: int, v: int) -> None:
        if u >= self.size or v >= self.size or u < 0 or v < 0:
            raise ValueError("Need to provide existing vertices")
        if v in self.adjacency_list[u]:
            self.adjacency_list[u].remove(v)
        else:
            print(f"{v} is not adjacent to {u}")
        # if u in self.adjacency_list[v]:  # Uncomment to make the graph undirected
        #     self.adjacency_list[v].remove(u)
        # else:
        #     print(f"{u} is not adjacent to {v}")

    def transpose(self) -> List[List[int]]:
        transposed: List[List[int]] = [[] for _ in range(self.size)]
        for i in range(len(self.adjacency_list)):
            for j in self.adjacency_list[i]:
                transposed[j].append(i)
        return transposed



