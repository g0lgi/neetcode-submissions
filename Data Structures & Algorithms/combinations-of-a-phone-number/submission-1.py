class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_char_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }

        output = []
        temp_string = ""

        def dfs(temp_string: str, curr_digits: str):
            curr_digit = curr_digits[0]
            curr_chars = digit_to_char_map[curr_digit]

            for char in curr_chars:
                temp_string += char
                if len(curr_digits) > 1:
                    dfs(temp_string, curr_digits[1:])
                else:
                    output.append(temp_string)
                temp_string = temp_string[:-1]

        dfs(temp_string, digits)

        return output