import random
class RandomizedSet(object):

    def __init__(self):
        self.indexMap = defaultdict(int) # val to index map
        self.list = []
        
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.indexMap:
            self.indexMap[val] = len(self.list) 
            self.list.append(val)
            return True
        return False
    
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.indexMap:
            index = self.indexMap[val]
            del self.indexMap[val]
            lastInsertedVal = self.list[-1]
            self.list[index] = lastInsertedVal
            self.list.pop()
            if lastInsertedVal in self.indexMap:
                self.indexMap[lastInsertedVal] = index
            return True
        return False
    
    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()