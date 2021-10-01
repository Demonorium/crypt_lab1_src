class Permuter:
    def __init__(self, table):
        self.table = table
    
    def encode(self, target: str):
        result = ''
        for i in range(len(target)):
            result += self.table[target[i]]
        
        return result
            
    
    