class Solution(object):
    def convertDateToBinary(self, date):
        # Step 1: split the date into year, month, and day
        parts = date.split('-')
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        
        # Step 2: convert each part to binary
        year_bin = bin(year)[2:]
        month_bin = bin(month)[2:]
        day_bin = bin(day)[2:]
        
        # Step 3: join them back with '-'
        binary_date = year_bin + '-' + month_bin + '-' + day_bin
        return binary_date