import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        alphabet = {}
        for task in tasks:
            alphabet[task] = alphabet.get(task, 0) + 1
        max_heap = []
        for key, value in alphabet.items():
            heapq.heappush(max_heap, (-value, key))
        process_queue = deque()
        cycles = 0
        while process_queue or max_heap:
            if not max_heap:
                cycles = abs(process_queue[0][2])
            else:
                freq_neg, task = heapq.heappop(max_heap)
                if freq_neg < -1:
                    process_queue.append((task, freq_neg + 1, cycles + n))
            if process_queue and process_queue[0][2] == cycles:
                task, freq_neg, _ = process_queue.popleft()
                heapq.heappush(max_heap, (freq_neg, task))
            cycles += 1
        return cycles