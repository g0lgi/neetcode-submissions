class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pointer1 = 0
        t_freqs = {}
        for char in t:
            t_freqs[char] = t_freqs.get(char, 0) + 1
        s_freqs = {}
        pointer2 = pointer1
        result = ""
        def is_valid():
            for char, count in t_freqs.items():
                if s_freqs.get(char, 0) < count:
                    return False
            return True
        while pointer2 < len(s):
            if s[pointer2] in t_freqs:
                s_freqs[s[pointer2]] = s_freqs.get(s[pointer2], 0) + 1
            while is_valid():
                valid_substring = s[pointer1:pointer2 + 1]
                if result == "":
                    result = valid_substring
                else:
                    if len(result) > len(valid_substring):
                        result = valid_substring
                if s[pointer1] in s_freqs:
                    s_freqs[s[pointer1]] -= 1
                pointer1 += 1
            pointer2 += 1
        return result