#include <numeric>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res_list;
        unordered_map<string, vector<string>> res_u_list;

        for (int i = 0; i < strs.size(); i++){
            // define the frequency array which will store the counts
            vector<int> frequency_array(26, 0);

            // iterate through each and every string of the vector of strings and update the frequency array
            for (auto character: strs[i]){
                frequency_array[character - 'a'] += 1;
            }

            // converting the frequency_array to frequency_string
            string frequency_string;

            for (int x : frequency_array) {
                frequency_string += to_string(x) + ',';
            }

            // appending the string as key and the actual string as a result inside the unordered_list
            res_u_list[frequency_string].push_back(strs[i]);
        }

        // below code is just to collect the values and return them
        for (auto& [key, values] : res_u_list) {
            res_list.push_back(values);
        }

        return res_list;
    }
};
