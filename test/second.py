example = ['a', 'b', 'c', 'd', 'e']


def find_repetetion(x):
    new_list = []
    for i in x:
        if i not in new_list:
            new_list.append(i)
        else:
            return i


a = find_repetetion(example)
print(a)
