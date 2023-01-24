a, b = map(int, input().split())
if b == 0:
    raise ZeroDivisionError('Нельзя делить на 0')
else:
    result = a / b
    print(result)
