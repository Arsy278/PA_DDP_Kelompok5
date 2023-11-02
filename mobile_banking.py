import os
import prettytable
os.system('cls')

import csv
from prettytable import PrettyTable

rekeningNasabah = [
    {'Nama': 'Muhammad Arsy Al-Fahd', 'Saldo': 0, 'PIN': 1111},
    {'Nama': 'Muhammad Abdul Khadir', 'Saldo': 0, 'PIN': 2222},
    {'Nama': 'Ali Khidir Kashimiri', 'Saldo': 0, 'PIN': 3333},
    {'Nama': 'Abdul Hamza ibn al-Muttalib', 'Saldo': 0, 'PIN': 4444},
    {'Nama': 'Fadhil ibn Al-Ghaniu', 'Saldo': 0, 'PIN': 5555}
]

#untuk sorting
# .sort()

dataAdmin = {
    'nama': 'arsy',
    'passAdmin': '1234'
}
def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilRekening():
    bersihkan_layar()
    tabel = PrettyTable(['Nama', 'Saldo'])
    for data in rekeningNasabah:
        tabel.add_row([data['Nama'], f"Rp {data['Saldo']:,.2f}".replace(",",".")])
    print(tabel)

def sortirSaldo():
    bersihkan_layar()
    rekeningNasabah.sort(key=lambda x: x['Saldo'], reverse=True)
    tampilRekening()
    print(f"{'-'*40:^40}")
    print(f"{'Saldo berhasil disortir.':^40}")
    print(f"{'-'*40:^40}")

def simpan_ke_csv():
    with open('mbanking.csv', 'w', newline='') as file:
        fieldnames = ['Nama', 'Saldo', 'PIN']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for data in rekeningNasabah:
            csv_writer.writerow(data)

def perbaruiRekening():
    bersihkan_layar()

    PIN = input("Masukkan PIN nasabah yang ingin dirubah: ")
    ditemukan = False

    for data in rekeningNasabah:
        if data['PIN'] == int(PIN):
            ditemukan = True
            print(f"Nama: {data['Nama']}")
            print(f"Saldo sekarang: Rp {data['Saldo']:,.2f}".replace(",", "."))
            opsi = input("Opsi yang ingin diubah (1: Nama, 2: Saldo, 3: PIN): ")

            if opsi == "1":
                nama_baru = input("Masukkan nama baru: ")
                data['Nama'] = nama_baru
                print("Nama berhasil diperbarui.")
            elif opsi == "2":
                saldo_baru = float(input("Masukkan saldo baru: "))
                data['Saldo'] = saldo_baru
                print("Saldo berhasil diperbarui.")
            elif opsi == "3":
                PIN_baru = int(input("Masukkan PIN baru: "))
                data['PIN'] = PIN_baru
                print("PIN berhasil diperbarui.")
    
    if ditemukan:
        simpan_ke_csv()
        print(f"Data rekening nasabah berhasil diubah.")
    else:
        print("PIN tidak valid atau nasabah tidak terdaftar.")
    
    print(f"{'-'*40:^40}")
    print(f"{'Daftar Rekening Nasabah':^40}")
    print(f"{'-'*40:^40}")

def setorUang():
    try:
        print("Silahkan memasukkan PIN sebelum melakukan penyetoran uang")
        PIN = int(input("Masukkan PIN anda: "))
        jumlah_uang = float(input("Masukkan jumlah uang: "))

        for data in rekeningNasabah:
            if data['PIN'] == int(PIN):
                data['Saldo'] += jumlah_uang

        bersihkan_layar()
        tampilRekening()
        simpan_ke_csv()
        print("Saldo berhasil ditambahkan.")
    except:
        print("Input tidak valid")

    bersihkan_layar()
    tampilRekening()
    print("Saldo Berhasil ditambahkan.")

def buatRekening():
    bersihkan_layar()
    print(f"{'-'*40:^40}")
    print(f"{'Buat Rekening Baru':^40}")
    print(f"{'-'*40:^40}")
    nama = input("Masukkan nama nasabah: ")
    pin = int(input("Buat PIN: "))
    saldo = float(input("Masukkan saldo awal (minimal 25rb): "))
    
    while True:
        if saldo < 25000:
            print("Gagal membuat rekening, saldo tabungan awal minimal Rp 25,000.")
        else:
            break

    rekening_baru = {'Nama': nama, 'Saldo': saldo, 'PIN': pin}
    rekeningNasabah.append(rekening_baru)

    simpan_ke_csv()
    tampilRekening()
    print("Rekening baru berhasil ditambahkan.")

def menuUtama():
    while True:
        print(f"{'-'*40:^40}")
        print(f"{'Livin by Mandiri':^40}")
        print(f"{'-'*40:^40}")
        print("1. Admin")
        print("2. Nasabah")
        print("3. Keluar")
        print(f"{'-'*40:^40}")
        opsi = input("Pilih menu (1/2/3): ")

        if opsi == "1":
            while True:
                print(f"{'-'*40:^40}")
                print(f"{'Pilih menu admin':^40}")
                print(f"{'-'*40:^40}")
                print("1. Informasi Nasabah")
                print("2. Sortir Saldo Nasabah")
                print("3. Buat rekening")
                print("4. Cari nasabah")
                print("5. Perbarui rekening nasabah")
                print("6. Hapus rekening nasabah")
                print("7. Kembali ke beranda")
                print("8. Keluar dari program.")
                print(f"{'-'*40:^40}")
                pilihan = input("Pilih Menu (1/2/3/4/5/6): ")

                if pilihan == "1":
                    bersihkan_layar()
                    tampilRekening()
                if pilihan == "2":
                    sortirSaldo()
                if pilihan == "3":
                    buatRekening()
                if pilihan == "5":
                    perbaruiRekening()
                if pilihan == "7":
                    bersihkan_layar()
                    menuUtama()
                if pilihan == "8":
                    bersihkan_layar()
                    print(f"{'-'*40:^40}")
                    print(f"{'Terima Kasih !':^40}")
                    print(f"{'-'*40:^40}")
                    break
            break
        if opsi == "2":
            while True:
                bersihkan_layar()
                print(f"{'-'*40:^40}")
                print(f"{'Pilih menu nasabah':^40}")
                print(f"{'-'*40:^40}")
                print("1. Buat rekening baru")
                print("2. Menabung")
                print("3. Kirim uang")
                print("4. Riwayat transaksi")
                print("5. Kembali ke beranda")
                print("6. Keluar dari program.")
                print(f"{'-'*40:^40}")
                pilihan = input("Pilih Menu (1/2/3): ")

                if pilihan == "1":
                    print("")
                if pilihan == "2":
                    setorUang()
                if pilihan == "5":
                    bersihkan_layar()
                    menuUtama()
                if pilihan == "6":
                    print(f"{'-'*40:^40}")
                    print(f"{'Terima Kasih !':^40}")
                    print(f"{'-'*40:^40}")
                    break
            break

        if opsi == "3":
            print(f"{'-'*40:^40}")
            print(f"{'Terima Kasih !':^40}")
            print(f"{'-'*40:^40}")
            break

menuUtama()