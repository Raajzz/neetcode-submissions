class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []

        i = 0

        for i in range(len(nums)):

            if i and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1
            target = -(nums[i])

            while(j < k):
                if (target == nums[j] + nums[k]):
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while(j < k and nums[j] == nums[j - 1]):
                        j += 1
                elif (target > nums[j] + nums[k]):
                    j += 1
                else:
                    k -= 1
        
        return res