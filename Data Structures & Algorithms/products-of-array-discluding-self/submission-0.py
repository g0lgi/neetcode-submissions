class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                if j != i:
                    temp = temp * nums[j]
            res.append(temp)
        return res  