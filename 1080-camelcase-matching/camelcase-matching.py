class Solution(object):
    def camelMatch(self, queries, pattern):
        
        def match(q, p):
            i = 0   # pointer for pattern
            
            for ch in q:
                # if characters match, move pattern pointer
                if i < len(p) and ch == p[i]:
                    i += 1
                # if uppercase appears and does NOT match pattern → fail
                elif ch.isupper():
                    return False
            
            # must match all pattern characters
            return i == len(p)

        return [match(q, pattern) for q in queries]
