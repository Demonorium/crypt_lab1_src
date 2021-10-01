from permute import Permuter
class MagicCube(Permuter):
    def __init__(self, cube):
        table = dict()
        c = 0
        for i in range(len(cube)):
            for j in range(len(cube)):
                table[c] = cube[i][j]-1
                c += 1

        Permuter.__init__(self, table)
        
