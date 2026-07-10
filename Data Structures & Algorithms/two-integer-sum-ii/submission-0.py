class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = len(numbers) - 1
        while pointer1 < pointer2:
            temp = numbers[pointer1] + numbers[pointer2]
            if temp > target:
                pointer2 -= 1
            elif temp < target:
                pointer1 += 1
            elif temp == target:
                return [pointer1 + 1, pointer2 + 1]