# Python標準ライブラリ
import collections
import os
import sys

# サードパーティライブラリ
import termcolor

# 同じ会社の別のチームが作ったライブラリ
import lesson_package

# ローカルファイル
import config

print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

print(sys.path)