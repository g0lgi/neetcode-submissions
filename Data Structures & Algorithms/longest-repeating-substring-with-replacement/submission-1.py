class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        pointer1 = 0
        pointer2 = 0
        longest_substring_length = 0
        temp_longest = 0
        while pointer1 <= pointer2 and pointer2 < len(s):
            chars[s[pointer2]] = chars.get(s[pointer2], 0) + 1
            char, most_frequent = max(chars.items(), key=lambda item: item[1])
            if ((pointer2 - pointer1 + 1) - most_frequent) > k:
                chars[s[pointer1]] = chars.get(s[pointer1], 0) - 1
                pointer1 += 1
                temp_longest -= 1
            pointer2 += 1
            temp_longest += 1
            if longest_substring_length < temp_longest:
                longest_substring_length = temp_longest
        return longest_substring_length
            