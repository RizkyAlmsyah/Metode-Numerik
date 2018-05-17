def fkuadrat(x,a,b,c):
    return a*x**2 +  b*x + c

def fpangkat3(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x + d

print("1.Ax^2 + Bx + C\n2.Ax^3 + Bx^2 + Cx + D\n")

pil = int(input("Masukkan Pilihan : "))
x0, x1, e = [float(i) for i in input("Masukkan X0, X1 dan Error : ").split()]
iterasi = 0
xn = x1
x_n_1=x0
if pil == 1:
    a, b, c = [float(i) for i in input("Masukan nilai ax^2 + bx + c: ").split()]
    print("No\t  xn\tf(xn)\t(xn)-(xn-1)\t\tf(xn)-f(xn-1)\t   Ex")
    print("=========================================================================")
    while abs(fkuadrat(xn ,a ,b ,c)) > e:
        selishx = xn - x_n_1
        selishkuadrat = fkuadrat(xn, a ,b ,c) - fkuadrat(x_n_1 ,a ,b ,c)
        xn1 = xn - (fkuadrat(xn, a ,b ,c)*selishx/selishkuadrat)
        er = abs(xn1 - xn) / abs(xn1)
        x_n_1 = xn
        xn = xn1
        iterasi += 1
        print(str(iterasi) + "\t%.3f" % xn + "\t%.3f" % fkuadrat(xn, a, b, c) + "\t%.3f" % selishx + "\t\t\t%.3f" % selishkuadrat + "\t\t\t%.3f" % er)
elif pil == 2:
    a, b, c, d= [float(i) for i in input("Masukan nilai ax^3 + bx^2 + cx + d: ").split()]
    print("No\t  xn\tf(xn)\t(xn)-(xn-1)\t\tf(xn)-f(xn-1)\t   Ex")
    print("=========================================================================")
    while abs(fpangkat3(xn ,a ,b ,c ,d)) >= e:
        selishx = xn - x_n_1
        selisihpangkat3 = fpangkat3(xn, a ,b ,c , d) - fpangkat3(x_n_1 ,a ,b ,c ,d)
        xn1 = xn - (fpangkat3(xn, a ,b ,c ,d)*selishx/selisihpangkat3)
        er = abs(xn1 - xn) / abs(xn1)
        x_n_1 = xn
        xn = xn1
        iterasi += 1
        print(str(iterasi)+"\t%.3f"%xn+"\t%.3f"%fpangkat3(xn, a, b, c, d)+"\t%.3f"%selishx + "\t\t\t%.3f"%selisihpangkat3 +"\t\t\t%.3f"%er)
else:
    print("Error")