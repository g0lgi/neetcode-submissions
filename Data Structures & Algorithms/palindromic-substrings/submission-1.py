class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        def palindromeCheck(l: int, r: int):
            nonlocal result
            result += 1
            while l > 0 and r < (len(s) - 1) and s[l-1] == s[r+1]:
                l -= 1
                r += 1
                result += 1

        for i in range(len(s)):
            if i < (len(s) - 1) and s[i] == s[i + 1]:
                palindromeCheck(i, i+1)
            palindromeCheck(i,i)

        return result

