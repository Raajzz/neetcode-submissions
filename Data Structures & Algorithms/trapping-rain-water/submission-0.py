class Solution:
    def trap(self, height: List[int]) -> int:
        # left max array

        left_max = 0
        left_max_array = []

        for h in height:
            left_max = max(left_max, h)
            left_max_array.append(left_max)

        # right max array

        right_max = 0
        right_max_array = []

        right_max = 0
        right_max_array = []

        for h in reversed(height):
            right_max = max(right_max, h)
            right_max_array.append(right_max)

        right_max_array.reverse()

        result = 0
        
        for index in range(1, len(height)-1):
            result += min(left_max_array[index], right_max_array[index]) - height[index]
        
        return result

