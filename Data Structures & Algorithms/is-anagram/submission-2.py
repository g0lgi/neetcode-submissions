class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dictS[s[i]] = dictS.get(s[i], 0) + 1
        for j in range(len(t)):
            dictT[t[j]] = dictT.get(t[j], 0) + 1
        print(dictS)
        print(dictT)
        for letter in dictS.keys():
            if dictS.get(letter, 0) != dictT.get(letter, 0):
                return False
        return True