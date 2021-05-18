example = ['a', 'b', 'c', 'd', 'c']


def find_repetition(x):
    new_list = []
    for i in x:
        if i not in new_list:
            new_list.append(i)
        else:
            return i


a = find_repetition(example)
print(a)
