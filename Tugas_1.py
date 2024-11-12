#Nama   = Moch. Yussar Rizky
#NIM    = 2403195
#Kelas  = RPL 1C

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Masukkan jumlah nilai Fibonacci yang ingin ditampilkan: "))
fibonacci(n)
