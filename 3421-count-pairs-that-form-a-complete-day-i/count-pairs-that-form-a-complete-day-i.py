class Solution(object):
    def countCompleteDayPairs(self, hours):
        seen = {}
        count = 0

        for h in hours:
            r = h % 24
            need = (24 - r) % 24

            if need in seen:
                count += seen[need]

            if r in seen:
                seen[r] += 1
            else:
                seen[r] = 1

        return count
