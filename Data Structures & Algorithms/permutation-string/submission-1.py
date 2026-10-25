class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        arr1 = [0]*26
        
        def get_arr(string, arr):
            for char in string:
                arr[ord(char) - ord('a')] += 1
        
        get_arr(s1, arr1)

        l = 0
        r = window_size

        while r <= len(s2):
            arr2 = [0]*26
            curr_string = s2[l:r]
            get_arr(curr_string, arr2)
            print(curr_string)
            if arr1 == arr2:
                return True
            l+=1
            r+=1

        return False

        