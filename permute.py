
def _get(string: str, index: int):
    if (index >= 0) and (index < len(string)):
        return string[index]
    return string[random.randint(0, len(string)-1)]

def _substring(string: str, f: int, count: int):
    result = ''
    for i in range(f, f+count):
        result += _get(string, i)
    return result

class Permuter:
    def __init__(self, table):
        self.decode_table = table
        self.table = {}
        for i in range(len(table)):
            self.table[table[i]] = i
        
    def encode(self, target: str):
        result = []
        for i in range(len(target)):
            result += _get(target, self.table[i])
        
        return ''.join(str(e) for e in result)
    
    def decode(self, target: str):
        result = ''
        for i in range(len(target)):
            result +=  _get(target, self.decode_table[i])
        
        return result

import random
    
class BlockPermuter(Permuter):
    def __init__(self, table):
        Permuter.__init__(self, table)
        
    def _get_block_count(self, target: str):
        t = len(target) % len(self.table)
        if t == 0:
            return len(target) // len(self.table)
        return (len(target) + len(self.table) - t) // len(self.table)
    def encode(self, target: str):
        result = ''
        block_count = self._get_block_count(target)
        
        for i in range(block_count):
            result += Permuter.encode(self, 
                _substring(target, i*len(self.table), len(self.table))
            )
        return result

    def decode(self, target: str):
        result = ''
        block_count = self._get_block_count(target)
        for i in range(block_count):
            result += Permuter.decode(self, 
                _substring(target, i*len(self.table), len(self.table))
            )
        return result
