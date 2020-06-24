# from lesson_package.talk import human
# from lesson_package.talk import animal
# from lesson_package.talk import *

# import *の書き方もあまり好ましくない（何が読み込まれるかすぐにわからないため）

# print(animal.sing())
# print(animal.cry())

# 関数から読み込むのではなく、モジュールから読み込むのが良い
# r = utils.say_twice('hello')
# print(r)

# print(human.sing())
# print(human.cry())

try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils

utils.say_twice('word')
