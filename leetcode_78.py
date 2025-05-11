class Solution:
    def sets(self, nums):
        all_sets = []
        def helper(j, adds):
            all_sets.append(adds)
            for i in range(j,len(nums)):
                helper(i+1, adds + [s[i]])
        helper(0, [])
        return all_sets

s = [1, 2, 3]
print(Solution().sets(s))
