class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        more_than_one_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                product = product * nums[i]
            else:
                more_than_one_zero += 1
        if more_than_one_zero > 1:
            result = [0] * len(nums)
        elif more_than_one_zero == 1:
            result = []
            for j in range(len(nums)):
                if nums[j] != 0:
                    result.append(0)
                else:
                    result.append(product)
        else:
            result = []
            for j in range(len(nums)):
                result.append(int(product / nums[j]))
        return result