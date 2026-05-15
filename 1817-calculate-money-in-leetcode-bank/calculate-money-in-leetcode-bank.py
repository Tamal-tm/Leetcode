class Solution(object):
    def totalMoney(self, n):
        # number of full weeks
        full_weeks = n // 7
        # remaining days after full weeks
        remaining_days = n % 7

        # money from full weeks: 
        # week1=28, week2=35, week3=42 → arithmetic series
        money = (full_weeks * 28) + (7 * full_weeks * (full_weeks - 1) // 2)

        # money from remaining days in the last (partial) week
        start = full_weeks + 1
        money += (remaining_days * (2 * start + (remaining_days - 1))) // 2

        return money