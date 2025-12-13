class Solution(object):
    def topKFrequent(self, words, k):
        freq = {}

        # Count frequency
        for w in words:
            freq[w] = freq.get(w, 0) + 1

        # Sort by:
        # 1) frequency descending
        # 2) word ascending (lexicographically)
        sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], w))

        return sorted_words[:k]
