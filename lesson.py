# x = 1;
# y = 2;
#
# x = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafafaaaa '
#
# def test_func(x, y, z,
#               faofejaofjafoja:ofjoawfjoafjeoagjhfjafoejafojfe='test'):
#     """
#
#     :param x:
#     :param y:
#     :param z:
#     :param faofejaofjafoja:
#     :return:
#
#     See details at: http://sakaijunfaofeja:ofjeaofjo//fawijofja:fawf/fjaojoifejejkdjfoejfefjwoafjawofjnjgoiejg:ajeofoe:
#     """
#
#     print('test')
#
# if x and y:
#     print('exist')
#
#     x = {'tets': 'sts'}
#
#     x, y = y, x
#
#     x = 100
#     yyyyyy = 200
#
# word = 'hello'
# word2 = '!'
#
# new_word = '{} $$$$$ {} !!!!!'.format(word, word2)
# new_word = word + '$$$$' + word2 + '!!!!!'
#
# long_word = ""
# for word in ['fafewaf', 'fafeaf', 'faef']:
#     long_word += "{}fafwaef".format(word)
#
# long_word = []
# for word in ['fafewaf', 'fafeaf', 'faef']:
#     long_word.append("{}fafwaef".format(word))
# new_long_word = ''.join(long_word)
#
# print('fafaofjawof')
# print("faefaffdffe")
# print("feond'fewafjojd")
#
# 'fafajofjaf {} fadf'.format('test')
# "fafajofjaf {} fadf".format('test')
#
# if x:
#     print('exit')
# else:
#     print('else')
#
# if x: print('exit')
# else: print('else')

def base(x):
    def plus(y):
        return x + y
    return plus

plus = base(10)
print(plus(10))
print(plus(30))

i = 0
def add_num():
    def plus(y):
        return i + y
    return plus

i = 10
plus = add_num()
print(plus(10))
i = 100
print(plus(30))