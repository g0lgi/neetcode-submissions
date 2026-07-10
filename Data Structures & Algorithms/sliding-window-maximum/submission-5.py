from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        result = []
        dq = deque()
        for i in range(len(nums)):
            if len(dq) == 0:
                dq.append(i)
            elif nums[i] < nums[dq[-1]]:
                dq.append(i)
            else:
                while len(dq) >= 1 and nums[dq[-1]] <= nums[i]:
                    dq.pop()
                dq.append(i)
            if i >= (k - 1):
                if dq[0] > (i - k):
                    result.append(nums[dq[0]])
                else:
                    while len(dq) >= 1 and dq[0] <= (i - k):
                        dq.popleft()
                    result.append(nums[dq[0]])
            # print(dq)
        return result