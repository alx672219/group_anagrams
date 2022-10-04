import collections
def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)   # defaultdict(list) = defining a dictionary with values as a list
        for s in strs:
            ans[tuple(sorted(s))].append(s)   # sort -> eat, ate, tea -> "aet"
        return ans.values()