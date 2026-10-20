class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix_product(nums.size(), 0);
        prefix_product[0] = nums[0];
        vector<int> suffix_product(nums.size(), 0);
        suffix_product[nums.size() - 1] = nums[nums.size() - 1];

        for (int i = 0; i < nums.size(); i++) {
            if ( i - 1 >= 0 ){
                prefix_product[i] = nums[i] * prefix_product[ i - 1 ];
            }
            int index = nums.size() - i - 1;
            if ( index + 1 < nums.size() ){
                suffix_product[index] = nums[index] * suffix_product[index + 1];
            }
        }

        vector<int> result(nums.size(), 0);

        // for(int i=0; i< nums.size(); i++){
        //     cout << "prefix: " << prefix_product[i] << endl << "suffix: " << suffix_product[i] << endl << endl;
        // }

        for(int i=0; i < nums.size(); i++){
            if (i + 1 == nums.size()){
                result[i] = prefix_product[i-1];
                continue;
            }
            if (i - 1 < 0){
                result[i] = suffix_product[i+1];
                continue;
            }
            result[i] = prefix_product[i-1]*suffix_product[i+1];
        }

        return result;

    }
};
