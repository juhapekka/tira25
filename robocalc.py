def calculate(input, rules):
    lista = list("L" + input + "R")
    paikka = 0
    tila = 1
    maxlooppi = 0
    
    while maxlooppi < 1000:
        maxlooppi += 1
        
        taa_symboli = lista[paikka]
        
        rule_saatu = False
        for rule in rules:

            rule_symboli, rule_tila, uus_symboli, uus_tila, action = rule
            if taa_symboli == rule_symboli and tila == rule_tila:
                rule_saatu = True

                lista[paikka] = uus_symboli
                tila = uus_tila

                if action == "LEFT":
                    paikka -= 1
                    if paikka < 0:
                        return False
                elif action == "RIGHT":
                    paikka += 1
                    if paikka >= len(lista):
                        return False
                elif action == "ACCEPT":
                    return True
                elif action == "REJECT":
                    return False
                else:
                    # reject.
                    return False
                break
        
        if not rule_saatu:
            # reject.
            return False

    # yli maximi loopin pituus
    return False

if __name__ == "__main__":
    rules = []

    rules.append(("L", 1, "L", 2, "RIGHT"))
    rules.append(("L", 3, "L", 2, "RIGHT"))

    rules.append(("0", 2, "X", 4, "RIGHT"))
    rules.append(("1", 4, "X", 5, "RIGHT"))
    rules.append(("1", 2, "X", 6, "RIGHT"))
    rules.append(("0", 6, "X", 7, "RIGHT"))

    rules.append(("0", 4, "0", 4, "RIGHT"))
    rules.append(("0", 5, "0", 5, "RIGHT"))
    rules.append(("0", 7, "0", 7, "RIGHT"))
    rules.append(("1", 6, "1", 6, "RIGHT"))
    rules.append(("1", 5, "1", 5, "RIGHT"))
    rules.append(("1", 7, "1", 7, "RIGHT"))

    rules.append(("X", 2, "X", 2, "RIGHT"))
    rules.append(("X", 4, "X", 4, "RIGHT"))
    rules.append(("X", 5, "X", 5, "RIGHT"))
    rules.append(("X", 6, "X", 6, "RIGHT"))
    rules.append(("X", 7, "X", 7, "RIGHT"))

    rules.append(("R", 2, "R", 2, "ACCEPT"))
    rules.append(("R", 4, "R", 4, "REJECT"))
    rules.append(("R", 6, "R", 6, "REJECT"))

    rules.append(("R", 5, "R", 3, "LEFT"))
    rules.append(("R", 7, "R", 3, "LEFT"))
    rules.append(("0", 3, "0", 3, "LEFT"))
    rules.append(("1", 3, "1", 3, "LEFT"))
    rules.append(("X", 3, "X", 3, "LEFT"))

    print(calculate("0", rules)) # False
    print(calculate("00", rules)) # False

    print(calculate("01", rules)) # True
    print(calculate("0110", rules)) # True
    print(calculate("0101", rules)) # True
    print(calculate("1000", rules)) # False
    print(calculate("00110101", rules)) # True
    print(calculate("00111101", rules)) # False
