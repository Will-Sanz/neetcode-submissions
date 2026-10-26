from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra: tracking earliest possible arrival time at each node, investigating earliest arrival next
        # track best known times in a map, and a min-heap for pending arrivals, earliest to latest

        # set up graph
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time))

        # starting node has time 0, everything else infinity
        store = defaultdict(lambda: float('inf'))
        store[k] = 0
        heap = []

        # put starting node in heap with time 0
        heapq.heappush(heap, (store[k], k))

        while heap:
            # take the earliest arrival out of the heap
            time, node = heapq.heappop(heap)

            # if entry time better than best time you have, take it
            if time > store[node]:
                continue

            # try every outgoing edge from that node (arrival + edge = possible arrival)
            for neighbor, c in graph[node]:
                total_cost = time + c
                if total_cost < store[neighbor]:
                    store[neighbor] = total_cost
                    heapq.heappush(heap, (total_cost, neighbor))

        return max(store.values()) if len(store) == n else -1