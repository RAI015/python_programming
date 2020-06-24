from lesson_package.tools import utils
# from ..tools import utils
# 相対パスはPythonではよろしくない書き方とのこと

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')