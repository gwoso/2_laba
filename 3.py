def third():
    a = []
    for x in range(200000001,200000100):
        b=set()  
        for n in range(2,round(x**0.5)+1):
            if x%n==0:
                b.add(n)
                b.add(x//n)
        if len(b)>5:
            b=sorted(b)
            mn=b[0]*b[1]*b[2]*b[3]*b[4]
            if mn<x:
                a.append(mn)
    return a[:5]
print(third())
