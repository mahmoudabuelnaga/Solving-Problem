class InstanceCount(object):
    count = 0
    def __init__(self, val):
        self.val = val
    
        InstanceCount.count += 1

    def setVal(self, NewVal):
        self.val = NewVal
    
    def getVal(self):
        return self.val
    
    def getCount(self):
        return self.count

a = InstanceCount(9)
b = InstanceCount(13)
c = InstanceCount(21)

for i in (a,b,c):
    print(i.getVal())
    print(i.getCount())