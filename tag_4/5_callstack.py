"""
Fehler Propagate
"""


def g():
    3 / 0


def f():
    g()


def fn():
    f()


def main():
    fn()


try:
    main()
except Exception as e:
    print(e)
