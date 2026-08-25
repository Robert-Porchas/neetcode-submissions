class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            wordLen = len(word)
            output += f"#{wordLen}#{word}"
        return output
    def decode(self, s: str) -> List[str]:
        output = []
        current = 0
        while current < len(s):
            if s[current] == "#" and s[current + 1].isdigit():
                if s[current + 2] != "#":
                    currentSpot = current + 1
                    lengthString = ""
                    while s[currentSpot] != "#":
                        lengthString += s[currentSpot]
                        currentSpot += 1
                        current += 1
                    length = int(lengthString)
                    current += 2
                else:
                    length = int(s[current + 1])
                    current += 3
                newWord = ""
                for i in range(length):
                    newWord += s[current + i]
                output.append(newWord)
                current += length
            else: 
                return output
        return output

