class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target == 0: return [[]]
        if target < 0: return []
        output = []
        for i in range(len(nums)):
            currOutput = self.combinationSum(nums[i:], target - nums[i])
            if len(currOutput) > 0:
                for listI in currOutput:
                    output.append([nums[i]] + listI)
        if len(output) > 0:
            return output    
        else:
            return []