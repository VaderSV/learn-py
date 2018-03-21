def transform(n):
    return lambda x: x + n


f = transform(4)
print(f(3))
