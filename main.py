def sum_all(*numbers:int|float|list[int|float])->int|float:
    total = 0
    for number in numbers:
        if isinstance(number, list):
            total += sum(number)
        else:
            total += number
    return total

if __name__ == '__main__':
    num = sum_all(4, 2, 3) # must return 9
    print(f'{num=}')
    num = sum_all([4, 2, 3]) # must return 9
    print(f'{num=}')
    num = sum_all([4, 2], 3) # must return 9
    print(f'{num=}')