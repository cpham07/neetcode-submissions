class Solution:

    def encode(self, strs: List[str]) -> str:
        words = ""
        
        for s in strs:
            words += str(len(s)) + "#" + s
        
        return words
    
    def decode(self, s: str) -> List[str]:
        backward = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]

            backward.append(word)

            i = j + 1 + length
        
        return backward




