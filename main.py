# ------------------------------------------
# Author:Skorobogatov Kirill
# ------------------------------------------

list_keys = [1, 2, 3]
list_values = ['one', 'two']

list_keys_ = [1, 2, 3]
list_values_ = ['one', 'two']

l1 = [1, 2, 3]
l2 = ['a','b']


# ------------------------------------------

def dict_from_keys_and_values(k, v):
    if len(k) > len(v):
      [v.append(None) for j in range(1, len(k) - len(v) + 1)]
    return dict(map(lambda key, value: (key, value), k, v))


print(' Result#1:', dict_from_keys_and_values(list_keys, list_values))
print(' Result#2:', dict_from_keys_and_values(list_keys_, list_values_))
print(' Result#3:', dict_from_keys_and_values(l1, l2))