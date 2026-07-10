class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        setLength = 0
        for num in nums:
            set1.add(num)
            if len(set1) == setLength:
                return True
            setLength = len(set1)
        return False

        