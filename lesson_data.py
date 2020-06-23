a = 1
b = 2

# a と b が等しい
print(a == b)

# a が b と異なる
print(a != b)

# a が b よりも小さい
print(a < b)

# a が b よりも大きい
print(a > b)

# a が b 以下である
print(a <= b)

# a が b 以上である
print(a >= b)

# a も b も真であれば真
if a > 0:
    if b > 0:
        print('a and b are positive')

if a > 0 and b > 0:
    print('a and b are positive')

# a または b が真であれば真
a = -1
b = 1
if a > 0:
    print('a or b is positive')
elif b > 0:
    print('a or b is positive')

if a > 0 or b > 0:
    print('a or b is positive')

