class OperationError(Exception):
    def __init__(self, op, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.op = op

    def __str__(self):
        return f'Операция "{self.op}" не является допустимой операцией'


operators = '+-*/'
try:
    a = int(input())
    b = int(input())
    op = input()
    if op not in operators:
        raise OperationError(op)
except ValueError:
    print('Ошибка ввода')
except OperationError as e:
    print(e)
else:
    match op:
        case '+':
            print(a + b)
        case '-':
            print(a - b)
        case '*':
            print(a * b)
        case '/':
            try:
                print(a / b)
            except ZeroDivisionError:
                print("Деление на ноль")
finally:
    print('The end')