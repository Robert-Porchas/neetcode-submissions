class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        # putting them in pairs so that we can sort them without losing speed
        carFleets = [] # will be the stack and output count
        for pos, spe in sorted(pairs, reverse=True):
            # iterate through the reverse sorted list to see which can combine
            current = (target - pos) / spe # how long we have until reach end 
            if len(carFleets) != 0 and current <= carFleets[-1]:
                continue
            else:
                carFleets.append(current)       
        return len(carFleets)