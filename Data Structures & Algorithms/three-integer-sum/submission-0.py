class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # the way to find the threeSum is by utilizing a loop + solution to twoSum

        # we'll get 3 indexes - i, j and k

        res = set()

        for i in range(0, len(nums)):

            # now the new array's range would be (i + 1) ... (len(nums) - 1)

            # twoSum solution

            sum_dict = {}

            target = -(nums[i])

            for j in range( i + 1, len(nums)):

                if (target - nums[j] in sum_dict):
                    triplet = tuple(sorted([nums[i], nums[j], target - nums[j]]))
                    res.add(triplet)
                    continue
                
                sum_dict[nums[j]] = j
            
        return [elem for elem in res]


