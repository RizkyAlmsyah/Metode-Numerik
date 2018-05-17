import math

def f(x):
    return x**2-x*6-16

a = float(input("Masukkan batas bawah = "))
b = float(input("Masukkan batas atas = "))
e = float(input("Masukkan Toleransi Error = "))
n = int(input("Masukkan Iterasi Maksimum = "))

print("\n")

if f(a) * f(b) > 0:
    print("Tidak ada akar")
else:
    kondisi = 1
    iterasi = 0
    while kondisi == 1:
        iterasi += 1
        xr =(a + b) / 2
        if abs(b-a) < e or iterasi > n:
            kondisi = 0
        elif f(a) * f(xr) == 0:
            break
        elif f(a) * f(xr) < 0:
            b = xr
        else:
            a = xr

        print(str(iterasi)+" "+str(xr)+" & "+str(f(xr)))

    print("\nx              y")
    print(str(xr)+" \t\t"+str(f(xr)))
