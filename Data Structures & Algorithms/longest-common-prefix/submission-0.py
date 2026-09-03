class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:        
        shortest_string = min(strs, key=len)
        prefix_string = ""
        for i in range(len(shortest_string)):
            curr_char = shortest_string[i] 
            for strings in strs:
                if  curr_char != strings[i]:
                    return prefix_string
            prefix_string += curr_char
        return prefix_string



        