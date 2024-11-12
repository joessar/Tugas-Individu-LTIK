def hitung_selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai):
    # Mengonversi waktu mulai dan selesai ke dalam detik
    waktu_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
    waktu_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai
    
    # Menghitung selisih waktu dalam detik
    selisih_detik = waktu_selesai - waktu_mulai

    # Mengonversi kembali selisih detik ke format jam, menit, detik
    selisih_jam = selisih_detik // 3600
    selisih_detik %= 3600
    selisih_menit = selisih_detik // 60
    selisih_detik %= 60

    return selisih_jam, selisih_menit, selisih_detik

# Input waktu mulai dan selesai
jam_mulai = int(input("Jam mulai: "))
menit_mulai = int(input("Menit mulai: "))
detik_mulai = int(input("Detik mulai: "))

jam_selesai = int(input("Jam selesai: "))
menit_selesai = int(input("Menit selesai: "))
detik_selesai = int(input("Detik selesai: "))

# Menghitung selisih waktu
selisih_jam, selisih_menit, selisih_detik = hitung_selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai)

# Menampilkan hasil
print(f"Selisih waktu: {selisih_jam} jam - {selisih_menit} menit - {selisih_detik} detik")
