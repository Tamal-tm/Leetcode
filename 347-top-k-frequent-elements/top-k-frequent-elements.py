class Solution(object):
    def topKFrequent(self, nums, k):
        seen = {}
        mylist = []

        # frequency map
        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1

        # sort by frequency (descending)
        sorted_items = sorted(seen.items(), key=lambda x: x[1], reverse=True)

        # take top k
        for value, freq in sorted_items:
            if k > 0:
                mylist.append(value)
                k -= 1
            else:
                break

        return mylist
