class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = int((left + right) / 2)
        while left < right:
            mid = int((left + right) / 2)
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]