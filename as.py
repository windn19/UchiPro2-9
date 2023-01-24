try:
    a, b = 1, 0# map(int, input().split())
    result = a / b
except Exception as e:
    print(e)
    print(e.args)
    print(e.__class__.__name__)