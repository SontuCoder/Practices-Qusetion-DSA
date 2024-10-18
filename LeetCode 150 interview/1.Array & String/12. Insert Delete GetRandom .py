# LeetCode: 380

import random
class Rendom:
    def __init__(self):    
        self.numMap = {}
        self.numList = []

    def insert(self,val):
        if(val in self.numMap):
            return False
        self.numMap[val] = len(self.numList)
        self.numList.append(val)
        return True

    def remove(self,val):
        if(val not in self.numMap):
            return False
        ind = self.numMap[val]
        self.numMap[self.numList[-1]]
        del self.numMap[val]
        self.numList[ind]=self.numList[-1]
        self.numList.pop()
        return True

    def getRendom(self):
        return random.choice(self.numList)


