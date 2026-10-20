class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_frequency = 0
        left = 0
        count = {}
        answer = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0)
            max_frequency = max(count[s[right]], max_frequency)

            while (right - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1
            
            answer = max(right - left + 1, answer)

        return answer