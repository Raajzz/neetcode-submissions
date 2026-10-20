class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # algorithm is this

        # have two pointer, `i` and `j`
        # move `j` pointer
        # always keep `i` at the lowest number possible

        i = 0
        j = 0

        res = 0

        while (j < len(prices)):

            res = max(res, prices[j] - prices[i])

            if (prices[j] < prices[i]):
                i = j
            
            j += 1
        
        return res
