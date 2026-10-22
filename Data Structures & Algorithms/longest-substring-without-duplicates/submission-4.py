class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # solution 1, moving the left index 1-by-1
        """
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
        """

        # solution 2, keeping track of the left index, so we jump directly left + 1

        index_tracker = {}

        left = 0
        right = 0
        res = 0

        for right in range(len(s)):
            if s[right] in index_tracker:
                left = max(index_tracker.pop(s[right]) + 1, left)
            index_tracker[s[right]] = right
            res = max(res, right - left + 1)
        
        return res
            

