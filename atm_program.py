import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Masukkan pin anda: "))
    trial = 0

    while (id != int(atm.cekPin()) and trial < 3):
        id = int(input("Pin anda salah. Silahkan masukkan lagi: "))
        trial += 1
        if trial == 3:
            print("Anda bukan pemilik ATM, balekno cok!")
            exit()
    while True:
        print("Selamat datang di Bank Ole Ole")
        print("\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar")
        pilihan = int(input("Masukkan pilihan anda: "))
        if pilihan == 1:
            print("Saldo anda sekarang "+ str(atm.cekSaldo())+ "\n")
        elif pilihan == 2:
            nominal = float(input("Masukkan nominal yang akan ditarik: "))
            verify_nominal = input("Apakah anda yakin akan menarik sebesar Rp. "+str(nominal)+" (y/n): ")
            if verify_nominal == "y":
                if nominal < atm.cekSaldo():
                    print("Saldo awal anda adalah "+str(atm.cekSaldo())+"")
                    atm.debit(nominal)
                    print("Transaksi berhasil!")
                    print("Saldo sisa sekarang adalah Rp. "+str(atm.cekSaldo())+"")
                else:
                    print("Saldo anda tidak cukup")
                    break
            else:
                break
        elif pilihan == 3:
            nominal = float(input("Masukkan nominal yang akan didepositkan: "))
            verify_nominal = input("Apakah anda yakin akan deposit sebesar Rp. "+str(nominal)+" (y/n): ")
            if verify_nominal == "y":
                atm.simpan(nominal)
                print("Transaksi berhasil!")
                print("Saldo anda sekarang adalah Rp. "+str(atm.cekSaldo())+"")
            else:
                print("break")
        elif pilihan == 4:
            repeat_pin = int(input("Masukkan pin lamamu: "))
            while repeat_pin != atm.cekPin():
                repeat_pin = int(input("Pin salah, silahkan masukkan "))
            if repeat_pin == atm.cekPin():
                update_pin = int(input("Silahkan masukkan pin yang baru: "))
                verify_pin = int(input("Masukkan ulang pin yang baru: "))
                if update_pin == verify_pin:
                    print("Pin berhasil diubah!")
                else:
                    print("Pin anda salah!")
                    break
            else:
                print("Error gaes!")
                break
        elif pilihan == 5:
            print("Resi tercetak otomatis saat anda keluar. \nHarap simpan tanda terima ini \nsebagai bukti transaksi anda.")
            print("No Record: "+ str(random.randint(100000,199999)))
            print("Tanggal Keluar: "+ str(datetime.datetime.now()))
            print("Saldo Akhir: Rp. "+ str(atm.cekSaldo()))
            print("Terima kasih telah menggunakan Bank Ole Ole!")
            exit()
        else:
            print("Error, silahkan pilih nomor sesuai menu diatas!")