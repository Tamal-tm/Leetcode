class Solution(object):
    def mostFrequentEven(self, nums):
        freq = {}
        max_count = 0
        answer = -1

        for n in nums:
            if n % 2 == 0:
                freq[n] = freq.get(n, 0) + 1

                if freq[n] > max_count or (freq[n] == max_count and n < answer):
                    max_count = freq[n]
                    answer = n

        return answer
