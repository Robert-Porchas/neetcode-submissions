class Solution:
    def maxArea(self, heights: List[int]) -> int:
        height1 = 0
        height2 = len(heights) - 1
        inH = 0
        outH = len(heights) - 1
        currentTotal = ((height2 - height1) * min(heights[height1], heights[height2]))
        while True:
            if inH == outH:
                break
            if ((outH - inH) * min(heights[inH], heights[outH]) > currentTotal):
                height1 = inH
                height2 = outH
                currentTotal = ((height2 - height1) * min(heights[height1], heights[height2]))
            if heights[inH] < heights[outH]:
                inH += 1
            else:
                outH -= 1
        return currentTotal
        