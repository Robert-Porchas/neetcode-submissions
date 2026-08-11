class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> freqMap;
        for(int i = 0; i < nums.size(); i++){
            if(freqMap.find(nums[i]) != freqMap.end()){
                return true;
            } else {
                freqMap.insert(nums[i]);
            }
        }
        return false;
    }
};