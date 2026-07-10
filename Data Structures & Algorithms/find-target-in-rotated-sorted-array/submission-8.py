class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        left = 0
        right = len(nums) - 1
        mid = int((left + right) / 2)
        while left < right:
            mid = int((left + right) / 2)
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        # print("after searching for min point:", nums[left], nums[mid], nums[right])

        if target <= nums[-1]:
            right = len(nums) - 1
        else:
            right = left - 1
            left = 0

        while left <= right:
            mid = int((right + left) / 2)
            # print("recalibrating which window to search", nums[left], nums[mid], nums[right])
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1