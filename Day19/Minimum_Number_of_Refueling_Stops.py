class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        # If starting fuel is already greater or equal to target, no need to 
        # refuel
        if startFuel >= target:
            return 0

        # Create a max heap to store the fuel capacities of stations
        max_heap = []
        i, n = 0, len(stations)
        stops = 0
        max_distance = startFuel

        # Loop until the car reaches the target or is out of fuel
        while max_distance < target:
            # Add fuel to the heap for stations within the current range
            while i < n and stations[i][0] <= max_distance:
                heapq.heappush(max_heap, -stations[i][1])
                i += 1

            # If there are no more stations in range and we can't reach the 
            # target, return -1
            if not max_heap:
                return -1

            # Refuel with the largest amount available and increment stops
            max_distance += -heapq.heappop(max_heap)
            stops += 1

        # Return the number of stops taken
        return stops
