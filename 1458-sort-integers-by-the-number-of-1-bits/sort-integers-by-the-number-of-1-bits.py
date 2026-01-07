class Solution(object):
    def sortByBits(self, arr):
        mylist = []
        result = []

        # store (count_of_1s, number)
        for i in range(len(arr)):
            binary = bin(arr[i])[2:]
            ones = 0
            for j in range(len(binary)):
                if binary[j] == '1':
                    ones += 1
            mylist.append((ones, arr[i]))

        # sort by count of 1s, then by number
        mylist.sort()

        for item in mylist:
            result.append(item[1])

        return result
