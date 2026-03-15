import random
angka = random.randint(1,10)
while True:
    tebak = int(input("Tebak angka dari 1 sampai 10: "))

    if tebak == angka:
        print("Selamat Anda Menang!")
        break
    else:
        print("Anda Kalah, coba lagi")
