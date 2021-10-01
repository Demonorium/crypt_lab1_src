import math
class PermutePathTable:
    def __init__(self, size_x):
        self.size_x = size_x
    def encode(self, target: str):
        result = ''
        size = len(target)
        for j in range(self.size_x):
            for i in range(math.ceil(size/self.size_x)):
            
                index=self.size_x*i+j
                if index >= size: result += ' '
                else: result += target[index]

        return result        
