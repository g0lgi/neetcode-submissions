class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_alphabet_count = [0] * 26
        for char in s1:
            s1_alphabet_count[ord(char) - ord("a")] += 1    
        print(s1_alphabet_count)
        left = 0
        right = left + len(s1) - 1
        while right < len(s2):
            substring_alphabet_count = [0] * 26
            for i in range(left, right + 1):
                substring_alphabet_count[ord(s2[i]) - ord("a")] += 1
            if substring_alphabet_count == s1_alphabet_count:
                return True
            print(s2[left], s2[right], substring_alphabet_count)
            left += 1
            right += 1
        return False