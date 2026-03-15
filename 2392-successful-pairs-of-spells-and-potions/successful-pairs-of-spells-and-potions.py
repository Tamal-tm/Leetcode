class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        suc_list = []
        n = len(potions)

        for s in spells:
            # Binary search for smallest potion where s * potion >= success
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if s * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            # All potions from 'left' to end work
            suc_list.append(n - left)

        return suc_list