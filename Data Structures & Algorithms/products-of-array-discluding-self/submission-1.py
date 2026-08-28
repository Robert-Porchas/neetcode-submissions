class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums) # each of these are O n
        post = [1] * len(nums)
        output = [] # using append will cut down on one more n
        currTotal = 1 # to keep count as we go down the line
        for i in range(len(nums)):
            pre[i] = currTotal
            currTotal *= nums[i]
        currTotal = 1
        for i in range(len(nums) - 1, -1, -1):
            post[i] = currTotal
            currTotal *= nums[i]
        for i in range(len(nums)):
            output.append(pre[i] * post[i])
        return output