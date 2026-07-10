class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = int((left + right) / 2)
        while left <= right:
            mid = int((left + right) / 2)
            # print(nums[left], nums[mid], nums[right])
            if nums[left] == target:
                return left
            if nums[mid] == target:
                return mid
            if nums[right] == target:
                return right
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    # print(1)
                    right = mid - 1
                else:
                    # print(2)
                    # print(nums[left], nums[mid], target)
                    left = mid + 1
            else:
                if nums[mid] <= nums[right]:
                    if nums[mid] <= target <= nums[right]:
                        # print(3)
                        left = mid + 1
                    else:
                        # print(4)
                        right = mid - 1
        return -1