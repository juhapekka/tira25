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

def create_rules():
    rules = []
    rules.append(('L', 1, 'L', 2, 'RIGHT')) # Aloitustila, ohitetaan 'L'

    # Tila 2: Luetaan ensimmäisen puoliskon ensimmäinen bitti
    rules.append(('0', 2, '0', 3, 'RIGHT')) # Jos '0', siirry tilaan 3, muista '0'
    rules.append(('1', 2, '1', 4, 'RIGHT')) # Jos '1', siirry tilaan 4, muista '1'
    rules.append(('R', 2, 'R', 0, 'REJECT')) # Jos 'R' heti alussa, hylkää (liian lyhyt syöte)

    # Tilat 3 ja 4: Luetaan ja verrataan loput ensimmäisestä puoliskosta ja siirrytään toiseen
    for i in range(5): # Maksimipituus 10, joten max 5 bittiä per puolisko
        # Tila 3: Oltiin luettu '0' alussa
        rules.append(('0', 3 + 2*i, '0', 3 + 2*i, 'RIGHT')) # Lue '0', pysy tilassa 3+2i
        rules.append(('1', 3 + 2*i, '1', 4 + 2*i, 'RIGHT')) # Lue '1', siirry tilaan 4+2i
        rules.append(('R', 3 + 2*i, 'R', 20, 'RIGHT')) # Ensimmäinen puolisko loppui, siirry tilaan 20 vertailua varten (alkuperäinen oli '0')

        # Tila 4: Oltiin luettu '1' alussa
        rules.append(('0', 4 + 2*i, '0', 4 + 2*i, 'RIGHT')) # Lue '0', pysy tilassa 4+2i
        rules.append(('1', 4 + 2*i, '1', 3 + 2*(i+1), 'RIGHT')) # Lue '1', siirry tilaan 3+2*(i+1)
        rules.append(('R', 4 + 2*i, 'R', 21, 'RIGHT')) # Ensimmäinen puolisko loppui, siirry tilaan 21 vertailua varten (alkuperäinen oli '1')


    # Tila 20: Verrataan toisen puoliskon bittejä, kun ensimmäinen oli '0'
    rules.append(('0', 20, '0', 22, 'RIGHT')) # Jos toinen puolisko alkaa '0', hyvä, siirry tilaan 22
    rules.append(('1', 20, '1', 0, 'REJECT')) # Jos alkaa '1', hylkää
    rules.append(('R', 20, 'R', 0, 'REJECT')) # Jos loppuu heti, hylkää

    # Tila 21: Verrataan toisen puoliskon bittejä, kun ensimmäinen oli '1'
    rules.append(('1', 21, '1', 22, 'RIGHT')) # Jos toinen puolisko alkaa '1', hyvä, siirry tilaan 22
    rules.append(('0', 21, '0', 0, 'REJECT')) # Jos alkaa '0', hylkää
    rules.append(('R', 21, 'R', 0, 'REJECT')) # Jos loppuu heti, hylkää

    # Tila 22: Verrataan loppuja bittejä
    for i in range(5):
        rules.append(('0', 22 + 2*i, '0', 22 + 2*i, 'RIGHT')) # Lue '0', pysy tilassa 22+2i
        rules.append(('1', 22 + 2*i, '1', 23 + 2*i, 'RIGHT')) # Lue '1', siirry tilaan 23+2i
        rules.append(('R', 22 + 2*i, 'R', 24, 'ACCEPT')) # Toinen puolisko loppui, hyväksy jos kaikki ok

        rules.append(('0', 23 + 2*i, '0', 22 + 2*(i+1), 'RIGHT')) # Lue '0', siirry takaisin vertailutilaan 22+2*(i+1)
        rules.append(('1', 23 + 2*i, '1', 23 + 2*i, 'RIGHT')) # Lue '1', pysy tilassa 23+2i
        rules.append(('R', 23 + 2*i, 'R', 0, 'REJECT')) # Toinen puolisko loppui kesken, hylkää


    rules.append(('R', 24, 'R', 24, 'ACCEPT')) # Viimeinen hyväksyntätila, jos ollaan tänne asti päästy ja 'R' luetaan, hyväksy.


    return rules

if __name__ == "__main__":
    rules = create_rules()

    print(calculate("00", rules)) # True
    print(calculate("001001", rules)) # True
    print(calculate("10111011", rules)) # True
    print(calculate("01", rules)) # False
    print(calculate("00100", rules)) # False
    print(calculate("10111101", rules)) # False