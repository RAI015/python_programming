# import lesson_package.utils
from lesson_package import utils
# from lesson_package import utils as u
# from lesson_package.utils import say_twice

# 関数から読み込むのではなく、モジュールから読み込むのが良い
r = utils.say_twice('hello')

print(r)