# タプルの使い所　appendが使えないことを逆手にとる
chose_from_two = ('A', 'B', 'C')
# chose_from_two = ['A', 'B', 'C']

answer = []
chose_from_two.append('A')
chose_from_two.append('C')

# answer.append('A')
# answer.append('C')

print(chose_from_two)
print(answer)