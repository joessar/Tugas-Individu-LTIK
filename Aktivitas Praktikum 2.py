#Nama   = Moch. Yussar Rizky
#NIM    = 2403195
#Kelas  = RPL 1C

angka = input("Masukkan angka (dipisahkan dengan( , ) : ")

def average(angka):
    angka = [int(i) for i in angka.split(",")]
    average = sum(angka)/len(angka)
    return average

print(f"Rata rata nya adalah:",average(angka))