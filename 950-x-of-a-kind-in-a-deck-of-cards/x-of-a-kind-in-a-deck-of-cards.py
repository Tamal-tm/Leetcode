class Solution(object):
    def hasGroupsSizeX(self, deck):
        if len(deck) < 2:
            return False

        seen = {}
        for num in deck:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        counts = list(seen.values())

        # find smallest count
        min_count = counts[0]
        for c in counts:
            if c < min_count:
                min_count = c

        # try to find a group size (X) that divides all counts
        for X in range(2, min_count + 1):
            good = True
            for c in counts:
                if c % X != 0:
                    good = False
                    break
            if good:
                return True

        return False