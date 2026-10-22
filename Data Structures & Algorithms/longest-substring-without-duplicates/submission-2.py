class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        res = 0

        freq_map = [0] * 256

        while(right < len(s)):
            if freq_map[ord(s[right])] == 0:
                freq_map[ord(s[right])] = 1
            else:
                # move the left pointer
                # remove elements till we reach s[left] == s[right]
                while(left < right):
                    if (s[left] == s[right]):
                        left += 1
                        break
                    else:
                        freq_map[ord(s[left])] = 0
                        left += 1
            
            res = max(res, right - left + 1)
            right += 1
        
        return res