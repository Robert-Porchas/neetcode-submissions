class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIndex = 0
        rightIndex = len(numbers) - 1
        while(True):
            totalSum = numbers[leftIndex] + numbers[rightIndex]
            if totalSum == target:
                return [leftIndex + 1, rightIndex + 1]
            if totalSum > target:
                rightIndex -= 1
                continue
            else:
                leftIndex += 1
            