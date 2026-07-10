class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        more_than_one_zero = 0
        index_of_zero = len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                product = product * nums[i]
            else:
                more_than_one_zero += 1
                index_of_zero = i
        if more_than_one_zero > 0:
            result = [0] * len(nums)
            if more_than_one_zero == 1:
                result[index_of_zero] = product    
        else:
            result = []
            for j in range(len(nums)):
                result.append(int(product / nums[j]))
        return result