angka = int(input("Masukkan angka bebas aja cik\n>"))

def hitung_genap(n):                            #reusable unit
    total_genap = 0
    for i in range(1, n + 1):                   
        if i % 2 == 0:
            total_genap += 1
    print("Jumlah angka genap", total_genap)

def hitung_ganjil(n):
    total_ganjil = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total_ganjil += 1
    print("Jumlah angka ganjil", total_ganjil)




if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap")

else:
    print(f"{angka} adalah bilangan ganjil")

if angka > 100:
    hitung_ganjil(angka)
    print(f"{angka} lebih besar dari 100 cuii")

elif angka == 100:
    hitung_genap(angka)
    print(f"{angka} sama cui ama 100")

else:
    hitung_genap(angka)
    print(f"{angka} lebih kecil dari 100")


