class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        pointer_1, pointer_2 = 0, 0
        result = 0
        while pointer_2 < len(s):
            while s[pointer_2] in unique_chars and pointer_1 < pointer_2:
                unique_chars.remove(s[pointer_1])
                pointer_1 += 1
            if (pointer_2 - pointer_1 + 1) > result:
                result = pointer_2 - pointer_1 + 1
            unique_chars.add(s[pointer_2])
            pointer_2 += 1
        return result