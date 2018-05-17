import math

print("Fungsi f(x) = exp(-x)-x")
xbawah = float(input("Masukkan batas bawah = "))
xatas = float(input("Masukkan batas atas = "))
n = float(input("Masukkan Jumlah pembagi N = "))
print("\n")

h = (xatas - xbawah) / n

x = {}
y = {}

i=0
while i <= n:
    x[i] = xbawah + i*h
    y[i] = math.exp(-x[i])-x[i]

    print(str(i+1)+" "+str(x[i])+" & "+str(y[i]))

    i+=1

j=0
while j <= n-1:
    if y[j]*y[j+1] < 0:
        print("\nTampilkan akar diantara "+ str(x[j])+" "+str(x[j+1]))
        if abs(y[j] < abs(y[j+1])):
            print("Akar Lebih dekat ke "+str(x[j]))
            fx = y[j]
        else:
            print("Akar Lebih dekat ke "+str(x[j+1]))
            fx = y[j+1]
        print("errornya "+ str(abs(fx)))

    j+=1