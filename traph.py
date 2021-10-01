
class Traph:
    def __init__(self, key):
        self.key = key  

    def get_rot0(self, x, y):
        return self.key[x][y]
    def get_rot1(self, x, y):
        return self.key[x][len(self.key)-1 - y]
    def get_rot2(self, x, y):
        return self.key[len(self.key) - x - 1][len(self.key)-y-1]
    def get_rot3(self, x, y):
        return self.key[len(self.key) - x - 1][y]
    
    def make_result(self, table):
        
        result = ''
        for i in range(len(self.key)):
            for j in range(len(self.key)):
                result += table[j][i]
        return result

    def encode(self, target:str):
        count = 0
        result_table = []
        for i in range(len(self.key)):
            lst = []
            for j in range(len(self.key)):
                lst.append('_')
            result_table.append(lst)

        for i in range(len(self.key)):
            for j in range(len(self.key)):
                if self.get_rot0(i, j) == 1:
                    result_table[i][j] = target[count]
                    count += 1
                    if count == len(target):
                        return self.make_result(result_table)
        
        for i in range(len(self.key)):
            for j in range(len(self.key)):
                if self.get_rot1(i, j) == 1:
                    result_table[i][j] = target[count]
                    count += 1
                    if count == len(target):
                        return self.make_result(result_table)
                        
        for i in range(len(self.key)):
            for j in range(len(self.key)):
                if self.get_rot2(i, j) == 1:
                    result_table[i][j] = target[count]
                    count += 1
                    if count == len(target):
                        return self.make_result(result_table)
        
        for i in range(len(self.key)):
            for j in range(len(self.key)):
                if self.get_rot3(i, j) == 1:
                    result_table[i][j] = target[count]
                    count += 1
                    if count == len(target):
                        return self.make_result(result_table)
        
        return self.make_result(result_table)