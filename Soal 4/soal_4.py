jumlah_tugas = int(input("Masukkan jumlah tugas (angka)\n>"))
daftar = []

priority_task = False

for i in range(1, jumlah_tugas + 1):
    judul = input("Judul tugas :\n>")
    prioritas = int(input("Prioritas : (1 - 3)\n>"))

    
    daftar.append({
        "Judul" : judul,
        "Prioritas" : prioritas
    })
                  


def kategori_prioritas(p):
    if p == 1:
        return "Tinggi"
    elif p == 2:
        return "Sedang"
    elif p == 3:
        return "Rendah"
    
for item in daftar:
    if item["Prioritas"] == 1:
        kategori_prioritas(item["Prioritas"])
        print("> "  + item["Judul"],"(" + kategori_prioritas(item["Prioritas"]) + ")")
        priority_task = True

if not priority_task:
    print("Tidak ada tugas prioritas tinggi")
     

            
            
            
