class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                count[index] += 1
            result[tuple(count)].append(string)
        return list(result.values())
