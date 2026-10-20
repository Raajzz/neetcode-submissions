class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solutions
        # 1. Store the frequencies on a dictionary and then sort
        # 2. Priority queue where the prioritzation is/will be done
        # by frequency
        # 3. Store a list of lists, [element, frequency], sort based on 
        # frequency in descending and take the element
        # 4. Create a list of lists, here index represent the number of
        # times an element apeared

        freq_list = [[]]
        freq_map = {}

        for i in range(len(nums)):
            freq_list.append([])
            if nums[i] not in freq_map:
                freq_map[nums[i]] = 1
            else:
                freq_map[nums[i]] += 1
        
        for key, value in freq_map.items():
            freq_list[value].append(key)
        
        res = []

        for freq_elem in reversed(freq_list):
            if len(freq_elem) != 0:
                res.extend(freq_elem)
            
            if (len(res) >= k):
                return res
        
        return res