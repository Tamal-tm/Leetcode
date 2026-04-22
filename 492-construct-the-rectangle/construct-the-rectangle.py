class Solution(object):
    def constructRectangle(self, area):
        w = int(area ** 0.5)  # Start from square root (closest possible width)
        while area % w != 0:
            w -= 1
        return [area // w, w]