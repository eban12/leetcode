class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacents = defaultdict(list)
        for num1, num2 in adjacentPairs:
            adjacents[num1].append(num2)
            adjacents[num2].append(num1)
        
        start = list(filter(lambda key: len(adjacents[key]) == 1, adjacents.keys())).pop()
        original = []
        added = set()
        while len(added) < len(adjacentPairs)+1:
            original.append(start)
            added.add(start)
            for adj in adjacents[start]:
                if adj not in added:
                    start = adj
                    break
        return original 
