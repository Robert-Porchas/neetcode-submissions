class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        indiceStack = []
        for i in range(len(temperatures)):
            while indiceStack and temperatures[i] > temperatures[indiceStack[-1]]:
                curr = indiceStack.pop()
                output[curr] = i - curr
            indiceStack.append(i)
        return output
