class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                new_left = s[l+1:r+1]
                new_right = s[l:r]
                return new_left == new_left[::-1] or new_right == new_right[::-1]
            l, r = l + 1, r - 1
        
        return True