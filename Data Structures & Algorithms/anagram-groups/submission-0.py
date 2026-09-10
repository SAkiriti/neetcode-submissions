from collections import defaultdict
from typing import List
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Store anagram groups
        res = defaultdict(list)

        #Go through each word
        for s in strs:
            # Count letters a-z
            count = [0] * 26   

            # Update letter counts
            for c in s:
                count [ord(c) - ord("a")] += 1

            #Add word to its matching anagram group
            res[tuple(count)].append(s)

        #Return all the groups
        return list(res.values())