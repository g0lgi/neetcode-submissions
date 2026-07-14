class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def dfs(curr_str: str, open_count: int, close_count: int):
            if len(curr_str) == (2*n):
                if open_count == close_count:
                    output.append(curr_str)
                return
            if open_count > close_count:
                curr_str += ")"
                dfs(curr_str, open_count, close_count + 1)
                curr_str = curr_str[:-1]
            curr_str += "("
            dfs(curr_str, open_count + 1, close_count)
            curr_str = curr_str[:1]
        
        dfs("(", 1, 0)

        return output