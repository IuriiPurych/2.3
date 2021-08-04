class Foo:
    pass


class Bar:
    pass


class One:
    pass


class Two:
    pass


class Some(Foo, Bar, One, Two):
    pass


var = Some.__mro__
print(var)
