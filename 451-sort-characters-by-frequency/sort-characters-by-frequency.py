class Solution(object):
    def frequencySort(self, s):
        seen = {}
        result_end = ""

        # Step 1: Count frequency of each character
        for char in s:
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] += 1

        # Step 2: Find and append characters by decreasing frequency
        while len(seen) > 0:
            max_key = None
            max_val = 0

            # Find the character with the highest frequency
            for key in seen:
                if seen[key] > max_val:
                    max_val = seen[key]
                    max_key = key

            # Add that character repeated 'max_val' times
            result_end += max_key * max_val

            # Remove it so we can find the next one
            del seen[max_key]

        return result_end