print('Перестановка')

key = 'cccabcccc'

key_set = set()
old_key = key
key = ''
for i in range(len(old_key)):
    if not old_key[i] in key_set:
        key += old_key[i]
        key_set.add(old_key[i])
print(key)

from permute import Permuter 
permuter = Permuter({
    0 : 1,
    1 : 2,
    2 : 4,
    3 : 0,
    4 : 3,
})

to_encode = "hello"
print('start:', to_encode)
encoded = permuter.encode(to_encode)
print('encoded:', encoded)
decoded = permuter.decode(encoded)
print('decoded:', decoded)

print('Блочная перестановка')
from permute import BlockPermuter
permuter = BlockPermuter({
    0 : 2,
    1 : 0,
    2 : 1
})

to_encode = "hello world"
print('start:', to_encode)
encoded = permuter.encode(to_encode)
print('encoded:', encoded)
decoded = permuter.decode(encoded)
print('decoded:', decoded)

print('Маршрутная перестановка')
from permutePathTable import PermutePathTable
permuter = PermutePathTable(6)

to_encode = "АБРАМОВ ИЛЬЯ СЕРГЕЕВИЧ"
print('start:', to_encode)
encoded = permuter.encode(to_encode)
print('encoded:', encoded)

print('Вертикальная перестановка')
from permuteVertical import PermuteVertical
permuter = PermuteVertical('ДЯДИНА')

to_encode = "АБРАМОВ ИЛЬЯ СЕРГЕЕВИЧ"
print('start:', to_encode)
encoded = permuter.encode(to_encode)
print('encoded:', encoded)


print('Поворотная решётка')
from traph import Traph
permuter = Traph([
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0]
])

to_encode = "АБРАМОВ+ДЯДИНА"
print('start:', to_encode)
encoded = permuter.encode(to_encode)
print('encoded:', encoded)


print('Магический квадрат')
from magicCube import MagicCube
permuter = MagicCube([
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
])

to_encode = "АБРАМОВ+ДЯДИНА.."
print('start:', to_encode)
encoded = permuter.encode(to_encode)
print('encoded:', encoded)
decoded = permuter.decode(encoded)
print('decoded:', decoded)



from multyPermute import MultyPermute
permuter = MultyPermute(4, 
{
    0:3,
    1:0,
    2:2,
    3:1
},
{
    0:2,
    1:0,
    2:3,
    3:1
})

to_encode = "АБРАМОВ+ДЯДИНА.."
print('start:', to_encode)
encoded = permuter.encode(to_encode)
print('encoded:', encoded)