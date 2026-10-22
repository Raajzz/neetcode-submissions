class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        res = 0

        freq_set = set()

        while(right < len(s)):
            while s[right] in freq_set:
                freq_set.remove(s[left])
                left += 1
            freq_set.add(s[right])
            res = max(res, right - left + 1)
            right += 1
        
        return res