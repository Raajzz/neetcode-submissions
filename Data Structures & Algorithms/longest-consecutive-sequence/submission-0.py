class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hash set method

        # we store the elements inside a hash set, then we check num - 1
        # if num - 1 is not inside the set, then `num` could be the number
        # we're looking for

        # we start checking num, num + 1, num + 2, ...
        # we also keep track of whenever a new element is inserted and store
        # that in res

        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        res = 0

        for num in nums:
            num_minus_1 = num - 1

            curr_count = 0

            if num_minus_1 not in nums_set:
                
                counter_num = num
                while counter_num in nums_set:
                    curr_count += 1
                    res = max(res, curr_count)
                    counter_num += 1
        
        return res

        # hash map method