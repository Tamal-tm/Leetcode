class Solution(object):
    def finalValueAfterOperations(self, operations):
        x=0
        for i in range(len(operations)):
            if '-'in operations[i]:
                x -=1
            elif '+' in operations[i]:
                x +=1
            else:
                continue
        return x
                
                
        
         