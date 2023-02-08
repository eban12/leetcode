class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        buses = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                buses[stop].append(bus)
        
        stopVisited = set()
        busTaken = set()
        queue = deque([(source, 0)])
        while queue:
            curStop, busesTaken = queue.popleft()
            stopVisited.add(curStop)
            if curStop == target:
                return busesTaken

            for bus in buses[curStop]:
                if bus in busTaken:
                    continue
                    
                busTaken.add(bus)
                for stop in routes[bus]:
                    if stop == target:
                        return busesTaken + 1

                    if stop not in stopVisited:
                        queue.append((stop, busesTaken+1))

        return -1
