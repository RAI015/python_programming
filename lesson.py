print('hello')
print("I don't know.")
print('I don\'t know.')
print('say "I don\'t know."')
print("say \"I don't know.\"")

print('hello. How are you?')
print('hello. \nHow are you?')
print(r'C:\name\name')

print('############')
print("""\
line1
line2
line3\
""")
print('############')

print('Hi.' * 3 + 'Mike.')

print('Py' + 'thon')
print('Py''thon')

prefix = 'Py'
print(prefix + 'thon')

s = ('aaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbb')

print(s)

word = 'Python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print('############')
print(word[0:2])
print(word[:2])
print('############')
print(word[2:])
word = 'j' + word[1:]
print(word[:])

n = len(word)
print(n)
