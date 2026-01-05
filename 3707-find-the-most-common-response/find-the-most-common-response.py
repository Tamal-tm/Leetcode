class Solution(object):
    def findCommonResponse(self, responses):
        mylist=[]
        seen={}
        for i in range(len(responses)):
            val=list(set(responses[i]))
            for j in range(len(val)):
                if val[j] in seen:
                    seen[val[j]] +=1
                else:
                    seen[val[j]] =1
        sorted_items = sorted(seen.items())
        max_key = max(sorted_items, key=lambda item: item[1])[0]

        return (max_key)