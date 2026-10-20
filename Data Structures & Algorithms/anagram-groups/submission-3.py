class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # res list

        res = []
        
        # dictionary to store all the ascii character as keys
        ascii_key_dict = {}

        # get the ascii representations
        for string in strs:

            ascii_list = [0] * 26

            for character in string:
                ascii_list[ord(character) - ord("a")] += 1
            
            ascii_string = ",".join(map(str, ascii_list))

            if ascii_string in ascii_key_dict:
                ascii_key_dict[ascii_string].append(string)
            else:
                ascii_key_dict[ascii_string] = [string]
        
        for key, value in ascii_key_dict.items():
            res.append(value)
        
        return res

