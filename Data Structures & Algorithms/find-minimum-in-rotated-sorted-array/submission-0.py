class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = nums[left]
        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            mid = int((right + left) / 2)
            print(nums[left], nums[mid], nums[right])
            result = min(result, nums[mid])    
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return result