class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> freqMap;
        for(int i = 0; i < nums.size(); i++){
            if(freqMap.find(nums[i]) != freqMap.end()){
                return true;
            } else {
                freqMap[nums[i]] = 1;
            }
        }
        return false;
    }
};