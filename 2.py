def second():
    num2 = 4**511 + 2**511 - 511
    dvoichka = bin(num2)[2:]
    return dvoichka.count('1')
print(second())
