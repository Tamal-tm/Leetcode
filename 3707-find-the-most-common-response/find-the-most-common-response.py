class Solution(object):
    def findCommonResponse(self, responses):
        seen = {}

        for r in responses:
            for x in set(r):   # count once per person
                if x in seen:
                    seen[x] += 1
                else:
                    seen[x] = 1

        max_freq = max(seen.values())
        answer = None

        for k in seen:
            if seen[k] == max_freq:
                if answer is None or k < answer:
                    answer = k

        return answer
