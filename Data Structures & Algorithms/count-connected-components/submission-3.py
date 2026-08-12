from collections import deque, defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def build_graph(edges):
            graph = defaultdict(list)
            for edge in edges:
                graph[edge[0]].append(edge[1])
                graph[edge[1]].append(edge[0])
            return graph
        
        graph = build_graph(edges)
        components = 0
        visited = set()
        for node in graph:
            if node not in visited:
                queue = deque([node])
                visited.add(node)
                while queue:
                    current = queue.popleft()
                    for neighbour in graph[current]:
                        if neighbour not in visited:
                            queue.append(neighbour)
                            visited.add(neighbour)
                    
                components += 1
        return components + n-len(visited)
        





                


