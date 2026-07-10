class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = int((right + left) / 2)
        print(nums[mid], target)
        while left <= right:
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
                mid = int((right + left) / 2)
            if nums[mid] > target:
                right = mid - 1
                mid = int((right + left) / 2)
            print(left, mid, right)
        return -1