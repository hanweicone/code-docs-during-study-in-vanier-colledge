knights = {'gallahad': 'the pure', 'robin': 'the brave'}

# loop use items()
for k, v in knights.items():
    print(k, v)
# loop use keys()
for k in knights.keys():
    print(k, knights[k])  # get value from key
# loop use values()
for v in knights.values():
    # get key from value,or you can revers keys and values
    # reversed_dictionary = dict(map(reversed, dictionary.items()))
    key = [key for key, value in knights.items() if value == v][0]
    print(key, v)
# reverse key and value,then it is easy use value(now becomes key) get key(now becomes value)
reverse_knights = {value: key for key, value in knights.items()}
print(reverse_knights)
# another way to get value from key
print(dict((v, k) for k, v in knights.items()).get('the pure'))
