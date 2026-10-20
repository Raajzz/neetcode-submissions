class Solution:

    def encode(self, strs: List[str]) -> str:

        if (len(strs)) == 0:
            return ""

        res = ""

        char_freq = "#"

        for string in strs:
            len_counter = 0
            for char in string:
                len_counter += 1
                res += char
            char_freq += str(len_counter) + ","
        
        if len(char_freq) > 1:
            char_freq = char_freq[:-1]

        res = res + char_freq

        return res

    def decode(self, s: str) -> List[str]:

        if s == "":
            return []

        res = []
        char_freq = ""

        for char in reversed(s):
            if char == "#":
                break
            char_freq += char

        char_freq = char_freq[::-1]
        char_freq_list = char_freq.split(",")
        start = 0

        for freq_elem in char_freq_list:
            int_freq_elem = int(freq_elem)
            res.append(s[start:(start + int_freq_elem)])
            start += int_freq_elem
        
        return res
