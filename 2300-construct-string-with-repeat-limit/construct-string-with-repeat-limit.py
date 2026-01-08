class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        from collections import Counter
        
        freq = Counter(s)
        chars = sorted(freq.keys(), reverse=True)
        result = []
        
        while chars:
            ch = chars[0]
            
            use = min(freq[ch], repeatLimit)
            result.append(ch * use)
            freq[ch] -= use
            
            if freq[ch] == 0:
                chars.pop(0)
            else:
                if len(chars) == 1:
                    break
                next_ch = chars[1]
                result.append(next_ch)
                freq[next_ch] -= 1
                if freq[next_ch] == 0:
                    chars.pop(1)
        
        return "".join(result)
