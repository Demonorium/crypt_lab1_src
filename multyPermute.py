from permute import Permuter

class MultyPermute:
    def __init__(self, size_x, permute_x, permute_y):
        self.permuter_x = Permuter(permute_x)
        self.permuter_y = Permuter(permute_y)
        self.size_x = size_x

    def encode(self, target: str):
        temp = ''
        result_array = []
        for i in range(len(target)):
            if (i+1)%self.size_x == 0:
                result_array.append(self.permuter_x.encode(temp))
                temp = ''
            temp += target[i]
        print(result_array)
        return self.permuter_y.encode(result_array)