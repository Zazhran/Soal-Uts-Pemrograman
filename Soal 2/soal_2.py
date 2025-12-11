jumlah_angka = 5

data = []

for i in range(1, jumlah_angka + 1):
    angka = int(input(f"Masukkan {jumlah_angka} angka, tinggal {jumlah_angka + 1 - i}\n> "))
    data.append(angka)

print(data)

def hitung_statistik(data):
    min = data[0]
    max = data[0]
    total = 0

    for n in data:
        if n < min:
            min = n
        elif n > max:
            max = n
        total += n

    avg = total / len(data)

    return min, max, avg


min, max, avg = hitung_statistik(data)

print("Angka min :", min)
print("Angka max :", max)
print("Rata rata :", avg)

if avg >= 80:
    print("Bagood :", avg)
elif avg >= 50:
    print("Cukub tahu :", avg)
else:
    print("Ewww :", avg)   


    

