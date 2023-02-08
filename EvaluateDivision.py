class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            value = values[i]
            graph[a].append((b, value))
            graph[b].append((a, 1/value))
        
        ans = []
        for a, b in queries:
            ans.append(self.findValue(a, b, graph, set()))
        return ans
    
    def findValue(self, a, b, graph, visited):
        if a not in graph: return -1
        
        if a == b: return 1

        visited.add(a)

        for child, v in graph[a]:
            if child not in visited:
                temp = self.findValue(child, b, graph, visited)
                if temp != -1: return v * temp
        return -1
