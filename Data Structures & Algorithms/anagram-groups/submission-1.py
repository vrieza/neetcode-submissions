class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            # Turn a string into sorted ones
            key = "".join(sorted(s))
            # Initialize the Key if its not "Seen"
            if key not in ans:
                ans[key] = []
            # Append the actual string
            ans[key] += [s]
        return list(ans.values())