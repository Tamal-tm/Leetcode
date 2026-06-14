class Solution(object):
    def findEvenNumbers(self, digits):
        res = []
        used = [0]*10
        for d in digits:
            used[d] += 1   # frequency table

        # Hundreds digit: 1–9 (cannot be 0)
        for a in range(1, 10):
            if used[a] == 0:
                continue
            used[a] -= 1

            # Tens digit: 0–9
            for b in range(10):
                if used[b] == 0:
                    continue
                used[b] -= 1

                # Units digit: must be even
                for c in (0,2,4,6,8):
                    if used[c] > 0:
                        res.append(a*100 + b*10 + c)

                used[b] += 1
            used[a] += 1

        return res