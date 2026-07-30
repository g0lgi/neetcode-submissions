class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def palindrome_check(t: str) -> bool:
            l = 0
            r = len(t) - 1

            while l < r:
                if t[l] != t[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        def dfs(u: str, curr: List[str]):
            if len(u) == 0:
                result.append(curr.copy())
                return

            if len(u) == 1:
                curr.append(u)
                # print(curr)
                result.append(curr.copy())
                curr.pop()
                return

            for j in range(1, len(u) + 1):
                slice = u[:j]
                if palindrome_check(slice):
                    curr.append(slice)
                    dfs(u[j:], curr)
                    curr.pop()
            return
        
        dfs(s, [])

        return result