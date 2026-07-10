class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        len1 = 0
        for str in strs:
            # brute force
            # sorted_str = "".join(sorted(str))
            # current_value = dict1.get(sorted_str, [])
            # current_value.append(str)
            # dict1[sorted_str] = current_value
            
            alphabet_count = [0] * 26
            for char in str:
                alphabet_count[ord(char) - ord("a")] += 1
            current_value = dict1.get(tuple(alphabet_count), [])
            current_value.append(str)
            dict1[tuple(alphabet_count)] = current_value
        return list(dict1.values())