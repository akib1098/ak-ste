class Solution:
    def merge(self, intervals):
        new = []
        for i in intervals:
            if not new or new[-1][1] < i[0]:
                new.append(i)
            else:
                new[-1][1] = max(new[-1][1], i[1])
        return new
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))