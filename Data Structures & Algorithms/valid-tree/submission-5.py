from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1 :
            return False
        ####
        #doesn't really check for connectivity
        # for edge in edges :
        #     visited.add(edge[0])
        #     visited.add(edge[1])
        
        # return not n - len(visited)
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        start = 0
        stack = [start]
        visited = set([start])
        while stack:
            current = stack.pop()
            for neighbour in graph[current]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.add(neighbour)
        return not n - len(visited)

        

        


         

           