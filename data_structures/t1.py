my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(my_tuple)
print(type(my_tuple))

print(f'Size => {len(my_tuple)}')

# indexing
print(f'Index 0 => {my_tuple[0]}')
print(f'Index 1 => {my_tuple[1]}')
print(f'last index => {my_tuple[-1]}')

# slicing
print(f'First 3 => {my_tuple[:3]}')
print(f'Last 3 => {my_tuple[-3:]}')

# tuple is immutable, gives error when trying to change
# my_tuple[0] = 100 