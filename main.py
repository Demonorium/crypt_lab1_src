print('Перестановка')

key = 'abcccc'

key_set = set()
old_key = key
key = [c for c in old_key if c not in old_key ]
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