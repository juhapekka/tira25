def check_year(year):
    ekat_kax = year // 100
    tokat_kax = year % 100
    summa = ekat_kax + tokat_kax
    nelioity = summa ** 2
    return nelioity == year

if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False