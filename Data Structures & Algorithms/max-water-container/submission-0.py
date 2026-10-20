class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        curr_height = 0
        max_height = 0

        while (i < j):
            curr_height = (j - i) * min(heights[j], heights[i]) 
            max_height = max(max_height, curr_height)

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        
        return max_height