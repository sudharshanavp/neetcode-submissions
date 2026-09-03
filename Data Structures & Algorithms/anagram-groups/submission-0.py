class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for strings in strs:
            sorted_key = "".join(sorted(strings))
            result[sorted_key].append(strings)
        return list(result.values())
        
            
            