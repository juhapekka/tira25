def evaluate(data):
    n = len(data)
    i = 0
    rval = []

    while i < n:
        if i <= n - 4 and (data[i:i+4] == "add(" or data[i:i+4] == "mul("):
            op = data[i:i+3]  # "add" tai "mul"
            j = i + 4

            if j < n and data[j].isdigit() and data[j] != '0':
                num1 = 0
                while j < n and data[j].isdigit():
                    num1 = num1 * 10 + (ord(data[j]) - ord('0'))
                    j += 1

                # pilkku
                if j < n and data[j] == ',':
                    j += 1

                    if j < n and data[j].isdigit() and data[j] != '0':
                        num2 = 0
                        while j < n and data[j].isdigit():
                            num2 = num2 * 10 + (ord(data[j]) - ord('0'))
                            j += 1
                        # sulkeva sulku
                        if j < n and data[j] == ')':
                            j += 1

                            # lasketaan
                            if op == "add":
                                res = num1 + num2
                            else:  # "mul"
                                res = num1 * num2

                            rval.append(str(res))
                            i = j  # siirrytään laskun jälkeen
                            continue

        # ei löytyny laskua
        rval.append(data[i])
        i += 1

    return "".join(rval)


if __name__ == "__main__":
    print(evaluate("add(1,2)")) # 3
    print(evaluate("aybabtu")) # aybabtu
    print(evaluate("mul(6,7),mul(7,191)")) # 42,1337
    print(evaluate("abadd(123,456)mulxmul(3,13)")) # ab579mulx39
    print(evaluate("mul()mul(13)mul(0,1)")) # mul()mul(13)mul(0,1)

    data = "mul(6,7)"*10**5
    result = evaluate(data)
    print(len(result)) # 200000
    print(result[:20]) # 42424242424242424242