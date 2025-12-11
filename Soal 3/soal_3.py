jumlah_item = int(input("masukkan barang\n"))

for i in range(1, jumlah_item + 1):
    nama_barang = "Indomie goreng kuah"
    harga = 10000
    qty = 5

    subtotal = harga * qty


total = subtotal * jumlah_item
print("Harga sebelum diskon :", total)


def diskon(total):
    if total >= 500000:
        potongan = total * 10 / 100
        print("dapat potongan 10%")

    elif total >= 300000:
        potongan = total * 5 / 100
        print("dapat potongan 5%")
    else:
        potongan = 0
        print("yahahhah ga dapet diskon(tol)")

    total_akhir = total - potongan
    return total_akhir, potongan

print("Total sesudah diskon :", diskon(total))
