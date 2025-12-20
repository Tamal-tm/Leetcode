class Solution(object):
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False

        # Case 1: strings already equal → need at least one duplicate char
        if s == goal:
            seen = set()
            for ch in s:
                if ch in seen:
                    return True
                seen.add(ch)
            return False

        diff = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        if len(diff) != 2:
            return False

        i, j = diff

        string_list = list(s)
        # swap instead of remove
        string_list[i], string_list[j] = string_list[j], string_list[i]

        new_string = "".join(string_list)

        return new_string == goal
