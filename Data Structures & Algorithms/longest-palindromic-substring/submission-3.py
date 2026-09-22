class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindromeCheck(l: int, r: int) -> str:
            # print(l, r)
            while l > 0 and r < (len(s) - 1) and s[l-1] == s[r+1]:
                l -= 1
                r += 1
            # print(s[l:r+1])
            return s[l:r+1]
        
        result = ''
        for i in range(len(s)):
            # print(i, s[i])
            if (i < (len(s) - 1)) and s[i] == s[i + 1]:
                temp = palindromeCheck(i, i+1)
                if len(temp) > len(result):
                    result = temp
            if (i > 0) and s[i] == s[i - 1]:
                temp = palindromeCheck(i-1, i)
                if len(temp) > len(result):
                    result = temp
            temp = palindromeCheck(i, i)
            if len(temp) > len(result):
                    result = temp
        
        return result