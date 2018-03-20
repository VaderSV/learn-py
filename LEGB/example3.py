x = 0


class X(object):

    y = x
    x = x + 1  # x is now a variable
    z = x

    def method(self):
        print(self.x)  # -> 1
        print(x)       # -> 0, the global x
        print(y)       # -> NameError: global name 'y' is not defined


inst = X()
print(inst.x, inst.y, inst.z, x) # -> (1, 0, 1, 0)
