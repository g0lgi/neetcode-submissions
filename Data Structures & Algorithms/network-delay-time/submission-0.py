class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency_dict = {}
        distances = {}

        for i in range(1, n + 1):
            adjacency_dict[i] = {}
            distances[i] = math.inf

        for edge in times:
            if edge[0] not in adjacency_dict:
                adjacency_dict[edge[0]] = {}
                distances[edge[0]] = math.inf
            adjacency_dict[edge[0]][edge[1]] = edge[2]
        
        distances[k] = 0

        pq = [(0, k)]

        print(adjacency_dict)

        while pq:
            curr_dist, curr_node = heapq.heappop(pq)

            if curr_dist > distances[curr_node]:
                continue

            for neighbor, time in adjacency_dict[curr_node].items():
                temp_dist = curr_dist + time

                if temp_dist < distances[neighbor]:
                    distances[neighbor] = temp_dist
                    heapq.heappush(pq, (temp_dist, neighbor))

        result = max(distances.values())
        if result == math.inf:
            return -1

        return result

        