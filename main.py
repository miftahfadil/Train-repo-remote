def sum_all(*numbers:int|float|list[int|float])->int|float:
    '''
    Menjumlahkan semua bilangan pada argumen
    :param *numbers: semua bilangan yang akan dijumlah

    :return: hasil penjumlahan semua argumen
    '''
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