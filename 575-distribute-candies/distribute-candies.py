class Solution(object):
    def distributeCandies(self, candyType):
        # Count how many different candy types there are
        unique_types = set(candyType)

        # She can only eat half the candies
        max_allowed = len(candyType) // 2

        # She gets the smaller of:
        #    (number of unique types) and (how many candies she can eat)
        return min(len(unique_types), max_allowed)