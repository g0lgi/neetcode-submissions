class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)

        def recursion(curr: int, depth=0) -> int:
            indent = "    " * depth
            # print(f"{indent}recursion({curr})")

            if curr > n:
                return 0
            
            if memo[curr] != -1:
                return memo[curr]
            if curr == n:
                return 1

            ways_from_here = recursion(curr + 1, depth + 1) + recursion(curr + 2, depth + 1)
            memo[curr] = ways_from_here
            return ways_from_here

        recursion(0)

        return memo[0]