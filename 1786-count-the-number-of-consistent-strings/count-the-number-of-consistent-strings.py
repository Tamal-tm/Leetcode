class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed_set = set(allowed)
        count = 0

        for word in words:
            is_valid = True
            for ch in word:
                if ch not in allowed_set:
                    is_valid = False
                    break
            if is_valid:
                count += 1

        return count
