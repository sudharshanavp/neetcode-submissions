class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        if len(s) == len(t) and s == t:
            return s

        tfreq, wfreq = {}, {}

        for char in t:
            tfreq[char] = 1 + tfreq.get(char, 0)
        print(tfreq)
        
        l = 0
        valid = 0
        required = len(t)
        pointers = [-1, -1]
        min_len = len(s) + 1

        for i in range(len(s)):
            char = s[i]
            wfreq[char] = 1 + wfreq.get(char, 0)

            if char in tfreq and wfreq[char] <= tfreq[char]:
                valid += 1
            
            while valid == required:
                if i - l + 1 < min_len:
                    min_len = i - l + 1
                    pointers = [l, i]
                
                wfreq[s[l]] -= 1
                if s[l] in tfreq and wfreq[s[l]] < tfreq[s[l]]:
                    valid -= 1
                l += 1
        
        l, i = pointers

        return s[l:i + 1] if min_len != len(s) + 1 else ""
