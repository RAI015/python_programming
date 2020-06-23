def test_func(x, l=[]):
    l.append(x)
    return l


# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)
#
# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)

r = test_func(100)
print(r)

# リストは参照渡しなので意図しない動きをする
# 暗黙のルールで、デフォルト引数にリストやディクショナリをするなというのがある
r = test_func(100)
print(r)


# 通常はこういう書き方をする方が好ましい
def test_func2(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func2(100)
print(r)

r = test_func2(100)
print(r)