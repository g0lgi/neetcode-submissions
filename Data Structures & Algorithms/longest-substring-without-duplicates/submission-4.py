class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicates = set()
        longest_substring_length = 0
        temp_substring_length = 0
        pointer1 = 0
        pointer2 = 0
        while pointer2 < len(s):
            if s[pointer2] not in duplicates:
                temp_substring_length += 1
                duplicates.add(s[pointer2])
                if temp_substring_length > longest_substring_length:
                    longest_substring_length = temp_substring_length
                pointer2 += 1
            else:
                duplicates.remove(s[pointer1])
                temp_substring_length -= 1
                pointer1 += 1
            print(pointer1, pointer2, duplicates, temp_substring_length, longest_substring_length)
        return longest_substring_length