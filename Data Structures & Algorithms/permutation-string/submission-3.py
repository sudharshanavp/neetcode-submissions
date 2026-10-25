class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        arr1 = [0]*26
        arr2 = [0]*26

        if window_size > len(s2):
            return False
        
        for i in range(window_size):
            arr1[ord(s1[i]) - 97] += 1
            arr2[ord(s2[i]) - 97] += 1

        if arr1 == arr2:
            return True

        for i in range(window_size, len(s2)):
            arr2[ord(s2[i]) - 97] += 1
            arr2[ord(s2[i - window_size])- 97] -= 1
            if arr1 == arr2:
                return True

        return False
        