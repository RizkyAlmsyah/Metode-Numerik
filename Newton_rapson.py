def fkuadrat(x,a,b,c):
    return a*x**2 +  b*x + c

def fpangkat3(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x + d

def fkuadrat_1(x,a,b):
    return 2*a*x + b

def fpangkat3_1(x,a,b,c):
    return 3*a*x**2 + 2*b*x + c

def flast(x, a, m ,k):
    return x**k -a**m

def flast_1(x, k):
    return k*x**(k-1)

print("1.Ax^2 + Bx + C\n2.Ax^3 + Bx^2 + Cx + D\n3.A^m/n")

pil = int(input("Masukkan Pilihan : "))
x0, e = [float(i) for i in input("Masukkan X0 dan Error : ").split()]
x = x0
iterasi = 1
if pil == 1:
    a, b, c = [float(i) for i in input("Masukan nilai ax^2 + bx + c: ").split()]
    print("No\t  x\t\tf(x)\tf'(x)\tEx")
    print("====================================")
    while abs(fkuadrat(x,a,b,c)) >= e:
        x1 = x-(fkuadrat(x,a,b,c))/fkuadrat_1(x,a,b)
        er = abs(x1 - x) / abs(x1)
        x = x1
        print(str(iterasi) + " \t%.3f"%x + "\t%.3f"%fkuadrat(x, a, b, c)+"\t%.3f"%fkuadrat_1(x,a,b)+"\t%.3f"%er)
        iterasi += 1
        if er <= e:
            break
elif pil == 2:
    a, b, c, d = [float(i) for i in input("Masukan nilai ax^3 + bx^2 + cx + d: ").split()]
    print("No\t  x\t\tf(x)\tf'(x)\tEx")
    print("====================================")
    while abs(fpangkat3(x,a,b,c,d)) >= e:
        x1 = x-fpangkat3(x,a,b,c,d)/fpangkat3_1(x,a,b,c)
        er = abs(x1 - x) / abs(x1)
        x = x1
        print(str(iterasi) + " \t%.3f"%x + "\t%.3f"%fpangkat3(x, a, b, c, d)+"\t%.3f"%fpangkat3_1(x, a, b, c)+"\t%.3f"%er)
        iterasi += 1
        if er <= e:
            break
elif pil == 3:
    a, m, k = [float(i) for i in input("Masukkan nilai a^(m/n) : ").split()]
    print("No\t  x\t\tf(x)\tf'(x)\tEx")
    print("====================================")
    while True:
        x1 = x-flast(x, a, m, k)/flast_1(x,k)
        er = abs(x1 - x) / abs(x1)
        x = x1
        print(str(iterasi)+" \t%.3f"%x + "\t%.3f"%flast(x, a, m, k)+"\t%.3f"%flast_1(x, k)+"\t%.3f"%er)
        iterasi += 1
        if er <= e:
            break
else:
    print("Error")


