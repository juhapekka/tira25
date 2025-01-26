def check_number(number:str):
    multipliers = [3, 7, 1, 3, 7, 1, 3, 7]
    
    if len(number) < 9 or not number[:-1].isdigit():
        return False
    
    if number[0] != '0':
        return False
    
    numba = sum(int(digit) * multipliers[i % len(multipliers)] for i, digit in enumerate(number[:-1]))
    if numba % 10 == 0:
        check_numba = 0
    else:
        check_numba = 10 - (numba % 10)

    if int(number[-1]) == check_numba:
        return True
    
    return False

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False
    print(check_number("3600242160")) #False