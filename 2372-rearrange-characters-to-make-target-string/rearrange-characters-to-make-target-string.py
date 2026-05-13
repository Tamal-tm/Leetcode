class Solution(object):
    def rearrangeCharacters(self, s, target):
        seen = {}
        for char in s:
            if char in target:
                if char in seen:
                    seen[char] += 1
                else:
                    seen[char] = 1

        # now check if all target chars are in seen
        # and find how many full target words we can form
        result = float('inf')

        for char in target:
            count_in_target = target.count(char)
            if char not in seen:
                return 0  # missing letter
            possible = seen[char] // count_in_target
            if possible < result:
                result = possible

        return result