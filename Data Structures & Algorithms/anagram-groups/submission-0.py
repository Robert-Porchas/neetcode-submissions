class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = {} # will be str int pair to check if ana has a spot
        currCount = 0 # will be the counter for next spot in output
        output = [] # to create the list of lists to return
        for item in strs:
            currString = "".join(sorted(item))
            if currString in anaMap:
                output[anaMap[currString]].append(item)
                # will add item in that group
            else: 
                anaMap[currString] = currCount # add a spot for this string
                currCount += 1 # add one for the next ana
                output.append([])
                output[anaMap[currString]].append(item)
                # will add next item
        return output