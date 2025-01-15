

def divide(first, second):
    if second == 0:
        return 'Ошибка'
    else:
        return first / second


if __name__ == '__main__':
    result = divide(20, 5)
    print(result)
