def my_filter(names):
    result = []
    for name in names:
        if len(name) <= 3:
            result.append(name)
    return result
names = ['12345', 'cat', 'manga', 'bob']
print(my_filter(names))
