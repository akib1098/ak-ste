class solution:
    def two_sum(self, nums, target):
        num_map = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in num_map:
                return [num_map[ans], i]
            num_map[nums[i]] = i
        return []