class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        boxes = {}

        for num in range(lowLimit, highLimit + 1):
            s = 0
            x = num
            while x > 0:
                s += x % 10
                x //= 10

            if s in boxes:
                boxes[s] += 1
            else:
                boxes[s] = 1

        return max(boxes.values())
