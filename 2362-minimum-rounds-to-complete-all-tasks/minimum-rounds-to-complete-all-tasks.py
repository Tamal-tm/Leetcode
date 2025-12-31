class Solution(object):
    def minimumRounds(self, tasks):
        seen = {}
        count = 0

        for t in tasks:
            seen[t] = seen.get(t, 0) + 1

        for freq in seen.values():
            if freq == 1:
                return -1
            count += freq // 3
            if freq % 3 != 0:
                count += 1

        return count
