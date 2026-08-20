class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        output = []
        for number in nums:
            if number in freqMap:
                freqMap[number] += 1
            else:
                freqMap[number] = 1
        sortedNumbers = sorted(freqMap, key=lambda x: freqMap[x], reverse = True)
        for i in range(0, k):
            output.append(sortedNumbers[i])
        return output