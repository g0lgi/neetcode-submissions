class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        len1 = 0
        for str in strs:
            sorted_str = "".join(sorted(str))
            current_value = dict1.get(sorted_str, [])
            current_value.append(str)
            dict1[sorted_str] = current_value
        return list(dict1.values())