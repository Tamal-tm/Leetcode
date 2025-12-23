class Solution(object):
    def numberOfPairs(self, nums):
        seen={}
        count=0
        rem=0
        mylist=[]
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] +=1
            else:
                seen[nums[i]] =1
        print(seen)
        
        for key, value in seen.items():
            if value % 2 == 0:
                count += value // 2
            else:
                count += value // 2
                rem +=1
        
        mylist.append(count)
        mylist.append(rem)
        return mylist