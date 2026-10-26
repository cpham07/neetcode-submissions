from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = []
        d = {}

        for i in strs:
            key = tuple(sorted(Counter(i).items()))
            if key not in d:
                d[key] = [i]
            else:
                d[key].append(i)
        
        for i in d:
            anagrams.append(d[i])

        return anagrams

        """
        for i, string1 in enumerate(strs):
            substring = [string1]
            for j, string2 in enumerate(strs):
                if (Counter(string1) == Counter(string2) and string1 != string2):
                    substring.append(string2)
            anagrams.append(substring)
            
        """
        # return anagrams
            

        