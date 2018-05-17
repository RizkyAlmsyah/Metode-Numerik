import math

def f(x):
    return k*x**2 + r*x + z

print("ax^2 + bx + c")
k = float(input("Masukkan a : "))
r = float(input("Masukkan b : "))
z = float(input("Masukkan c : "))
a = float(input("Masukkan batas atas : "))
b = float(input("Masukkan batas bawah : "))
e = float(input("Toleransi error : "))
n = int(input("Iterasi Maksimum : "))

print("\n Fungsi= "+str(k)+"x^2 "+str(b)+"x "+str(z)+"\n")
print("no  a\t  f(a)\tb\t  f(b)\tw\t   c\tf(c)")
if f(a)*f(b) < 0:
    kondisi = 1
    iterasi = 0
    while kondisi == 1:
        iterasi += 1
        w = f(a)/(f(a)-f(b))
        c = a + w*(b-a)
        if abs(b-a) < e or iterasi > n:
            kondisi = 0
        elif f(a)*f(c) < 0:
            b = c
        else:
           a = c

        print(str(iterasi-1)+" %.2f "%a+" %.2f "%f(a)+" %.2f "%b+" %.2f "%f(b)+" %.2f "%w+" %.2f "%c+" %.2f "%f(c))

    print("\n%.2f"%c+" %.2f"%f(c))
else:
    print("tampilkan tidak ada akar")
