class Solution(object):
    def majorityFrequencyGroup(self, s):
        freq = {}
        
        # Step 1: count frequency of each character
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        
        groups = {}
        
        # Step 2: group characters by frequency
        for ch, f in freq.items():
            if f in groups:
                groups[f].append(ch)
            else:
                groups[f] = [ch]
        
        max_size = 0
        best_freq = 0
        
        # Step 3: find majority frequency group
        for f, chars in groups.items():
            if len(chars) > max_size or (len(chars) == max_size and f > best_freq):
                max_size = len(chars)
                best_freq = f
        
        # Step 4: return result
        return "".join(groups[best_freq])
