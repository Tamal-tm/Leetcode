class Solution:
    def maxScore(self, cardPoints, k):
        if k == len(cardPoints):
            return sum(cardPoints)

        left_sum = 0
        right_sum = 0
        max_sum = 0
        n = len(cardPoints)

        # take k from left
        for i in range(k):
            left_sum += cardPoints[i]
        
        max_sum = left_sum

        right_index = n - 1

        # slide
        for i in range(k - 1, -1, -1):
            left_sum -= cardPoints[i]
            right_sum += cardPoints[right_index]
            right_index -= 1
            
            curr = left_sum + right_sum
            if curr > max_sum:
                max_sum = curr

        return max_sum