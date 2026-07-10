import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_dict = {}
        for task in tasks:
            tasks_dict[task] = tasks_dict.get(task, 0) + 1
        
        task_priority = []
        for task, freq in tasks_dict.items():
            heapq.heappush(task_priority, (-freq, task))
        
        task_queue = deque()
        cycles = 0
        while task_queue or task_priority:
            if not task_priority:
                cycles = task_queue[0][2]
            else:
                freq_neg, task = heapq.heappop(task_priority)
                if freq_neg < -1:
                    task_queue.append((freq_neg + 1, task, cycles + n))
            
            if task_queue and cycles == task_queue[0][2]:
                freq_neg, task, _ = task_queue.popleft()
                heapq.heappush(task_priority, (freq_neg, task))
            cycles += 1

        return cycles