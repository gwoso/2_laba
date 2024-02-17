from itertools import product
def first():
    cnt = 0
    arr = []
    alphabet = "ABCDE"
    biba = product(alphabet, repeat = 5)
    for word in biba:
        arr.append(list(word))
    for i in arr:
        if i[0] != 'E' and i[4] != 'A':
            cnt += 1
    return cnt
print(first())
