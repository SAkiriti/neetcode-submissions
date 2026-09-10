class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Store anagram groups
        res = defaultdict(list)
        
        # Go through each word
        for s in strs:

             # Sort letters to make a key
            sortedS = ''.join(sorted(s))

             # Add word to matching group
            res[sortedS].append(s)

         # Return all groups
        return list(res.values())