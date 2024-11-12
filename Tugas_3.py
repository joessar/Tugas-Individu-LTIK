#Nama   = Moch. Yussar Rizky
#NIM    = 2403195
#Kelas  = RPL 1C

print("Input mulai:")
jam_mulai = int(input("Jam: "))
menit_mulai = int(input("Menit: "))
detik_mulai = int(input("Detik: "))

print("Input selesai:")
jam_selesai = int(input("Jam: "))
menit_selesai = int(input("Menit: "))
detik_selesai = int(input("Detik: "))

def selisih():
    jam = jam_selesai - jam_mulai
    menit = menit_selesai - menit_mulai
    detik = detik_selesai - detik_mulai

    if detik < 0:
        detik += 60
        menit -= 1

    if menit < 0:
        menit += 60
        jam -= 1 
    
    if jam_selesai < jam_mulai:  #kemungkinan dapat terjadi apabila pelari telah berlari hampir 24 jam
        jam += 24

    return jam, menit, detik

jam, menit, detik = selisih()
print("Hitung selisih: ")
print(f"{jam} jam, {menit} menit, {detik} detik")