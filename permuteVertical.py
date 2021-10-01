import math
class PermuteVertical:
    def __init__(self, key: str):
        self.size_x = len(key)
        self.coder = {}
        
        ts = set()
        
        mx = -1
        for i in range(self.size_x):
            if ord(key[i]) > mx:
                mx = ord(key[i])
        mn = mx
        mn_v = -1
        for i in range(self.size_x):
            mn = mx
            for j in range(self.size_x):
                if ord(key[j]) <= mn and not j in ts:
                    mn = ord(key[j])
                    mn_v = j
            
            ts.add(mn_v)
            self.coder[i] = mn_v
        

    def encode(self, target: str):
        result = ''
        size = len(target)
        for tj in range(self.size_x):
            j = self.coder[tj]
            for i in range(math.ceil(size/self.size_x)):
                index = self.size_x*i+j
                if index >= size: result += ' '
                else: result += target[index]

        return result        
