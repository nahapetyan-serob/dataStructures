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

    def dfs_traverse(self) -> None:
        visited = [False] * self.size
        for u in range(self.size):
            if not visited[u]:
                self.dfs(u, visited)

    def dfs(self, u: int, visited: List[bool]) -> None:
        visited[u] = True
        for v in self.adjacency_list[u]:
            if not visited[v]:
                self.dfs(v, visited)
        print(f"Traversed through {u}")

    def bfs(self, src: int) -> None:
        visited = [False] * self.size
        visited[src] = True
        queue = [src]
        while queue:
            u = queue.pop(0)
            for v in self.adjacency_list[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)

    def has_cycle_undirected(self) -> bool:
        visited = [False] * self.size
        for u in range(self.size):
            if not visited[u]:
                if self.has_cycle_undirected_dfs(u, visited, -1):
                    return True
        return False

    def has_cycle_undirected_dfs(self, vertex: int, visited: List[int], parent: int) -> bool:
        visited[vertex] = True
        for v in self.adjacency_list[vertex]:
            if not visited[v]:
                if self.has_cycle_undirected_dfs(v, visited, vertex):
                    return True
            elif v != parent:
                return True
        return False

    def has_cycle_directed(self) -> bool:
        visited = [False] * self.size
        on_stack = [False] * self.size
        for v in range(self.size):
            if not visited[v]:
                if self.dfs_directed_cycle(v, visited, on_stack):
                    return True
            elif on_stack[v]:
                return True
        return False

    def dfs_directed_cycle(self, vertex: int, visited: List[bool], on_stack: List[bool]) -> bool:
        visited[vertex] = True
        on_stack[vertex] = True
        for u in self.adjacency_list[vertex]:
            if not visited[u]:
                return self.dfs_directed_cycle(u, visited, on_stack)
            elif on_stack[u]:
                return True
        on_stack[vertex] = False
        return False

    def all_paths(self, src: int, dst: int) -> List[List[int]]:
        tmp = []
        paths = []
        visited = [False] * self.size
        self.dfs_all_paths(src, dst, tmp, paths, visited)
        return paths

    def dfs_all_paths(self, u: int, dst: int, tmp: List[int], paths: List[List[int]], visited: List[bool]) -> None:
        visited[u] = True
        tmp.append(u)
        if u == dst:
            paths.append(tmp[:])
        else:
            for vertex in self.adjacency_list[u]:
                if not visited[vertex]:
                    self.dfs_all_paths(vertex, dst, tmp, paths)
        tmp.pop()
        visited[u] = False

    def topological_sort(self) -> List[int]:
        ts = []
        visited = [False] * self.size
        on_stack = [False] * self.size
        try:
            for v in range(self.size):
                if not visited[v]:
                    self.dfs_top_sort(v, ts, visited, on_stack)
        except ValueError as e:
            print(e)
        return ts[::-1]

    def dfs_top_sort(self, vertex: int, ts: List[int], visited: List[bool], on_stack: List[bool]) -> None:
        visited[vertex] = True
        on_stack[vertex] = True
        for u in self.adjacency_list[vertex]:
            if not visited[u]:
                self.dfs_top_sort(u, ts, visited, on_stack)
            elif on_stack[u]:
                raise ValueError('Has a cycle')
        on_stack[vertex] = False
        ts.append(vertex)

    def get_in_degree(self) -> List[int]:
        in_degree = [0] * self.size
        for u in range(self.size):
            for v in self.adjacency_list[u]:
                in_degree[v] += 1
        return in_degree

    def kahn(self) -> List[int]:
        ts = []
        in_degree = self.get_in_degree()
        queue = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            u = queue.pop(0)
            ts.append(u)
            for v in self.adjacency_list[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if len(ts) != self.size:
            print('Has a cycle')
            return []
        else:
            return ts

    def shortest_path(self, src: int, dst: int) -> List[int]:
        visited = [False] * self.size
        visited[src] = True
        queue = [src]
        paths = [[src]]
        while queue:
            u = queue.pop(0)
            tmp = paths.pop(0)
            if u == dst:
                return tmp
            for v in self.adjacency_list[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
                    paths.append(tmp + [v])
        return []




