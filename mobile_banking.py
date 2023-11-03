from datetime import datetime 
import os
os.system('cls')

import pwinput
import csv
from prettytable import PrettyTable

rekeningNasabah = [
    {'Nama': 'Muhammad Arsy Al-Fahd', 'Saldo': 0, 'PIN': 1111},
    {'Nama': 'Muhammad Abdul Khadir', 'Saldo': 0, 'PIN': 2222},
    {'Nama': 'Ali Khidir Kashimiri', 'Saldo': 0, 'PIN': 3333},
    {'Nama': 'Abdul Hamza ibn al-Muttalib', 'Saldo': 0, 'PIN': 4444},
    {'Nama': 'Fadhil ibn Al-Ghaniu', 'Saldo': 0, 'PIN': 5555}
]

dataAdmin = {
    'nama': 'arsy',
    'passAdmin': '1234'
}

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def simpan_ke_csv():
    with open('mbanking.csv', 'w', newline='') as file:
        fieldnames = ['Nama', 'Saldo', 'PIN']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for data in rekeningNasabah:
            csv_writer.writerow(data)

def setorUang():
    print(f"{'-'*40:^40}")
    print(f"{'Setor Uang':^40}")
    print(f"{'-'*40:^40}")
    try:
        print("Silahkan memasukkan PIN sebelum melakukan penyetoran uang")
        PIN = pwinput.pwinput("Masukkan PIN anda: ", mask='*')
        PIN = int(PIN)

        pin_benar = False
        for data in rekeningNasabah:
            if data['PIN'] == PIN:
                pin_benar = True
                break

        if pin_benar:
            jumlah_uang = int(input("Masukkan jumlah uang: "))
            if jumlah_uang < 0:
                print("Masukkan saldo yang benar.")
            else:
                for data in rekeningNasabah:
                    if data['PIN'] == int(PIN):
                        data['Saldo'] += jumlah_uang
                        tabel = PrettyTable(['Nama', 'Saldo'])
                        tabel.add_row([data['Nama'], f"Rp {data['Saldo']:,.2f}".replace(",",".")])
                        print(tabel)
                        simpan_ke_csv()
                        print("Saldo berhasil ditambahkan.")
                        pilihanNasabah = input(str("Tampilkan Saldo ? (ya/tidak): "))
                        if pilihanNasabah == "ya":
                            bersihkan_layar()
                            temukanNasabah = False
                            for data in rekeningNasabah:
                                if data['PIN'] == PIN:
                                    temukanNasabah = True
                                    tabel = PrettyTable(['Nama', 'Saldo'])
                                    tabel.add_row([data['Nama'], f"Rp {data['Saldo']:,.2f}".replace(",",".")])
                                    print(tabel)
                                    break
                            if not temukanNasabah:
                                print("PIN Salah atau nasabah tidak ditemukan.")
                                input("Tekan Enter untuk kembali...")
                        else:
                            menuUtama()
        else:
            print("PIN Salah.")
            while True:
                pilihan = input("Ketik 1 untuk kembali ke menu utama: ")
                if pilihan == "1":
                    menuUtama()
                    break
                else:
                    print("Hanya diperbolehkan Memasukkan angka 1.")

    except:
        print("Input tidak valid")

def transferUang():
    bersihkan_layar()
    try:
        print("Silahkan memasukkan PIN sebelum melakukan transfer uang")
        dataPengirim = pwinput.pwinput("Masukkan PIN Anda: ", mask='*')
        dataPengirim = int(dataPengirim)

        pin_benar = False
        for data in rekeningNasabah:
            if data['PIN'] == dataPengirim:
                pin_benar = True
                break

        if not pin_benar:
            print("PIN Salah.")
            while True:
                pilihan = input("Ketik 1 untuk kembali ke menu utama: ")
                if pilihan == "1":
                    menuUtama()
                    return
                else:
                    print("Hanya diperbolehkan memasukkan angka 1.")

        print("Masukkan informasi penerima:")
        dataPenerima = pwinput.pwinput("Masukkan PIN penerima: ", mask='*')
        dataPenerima = int(dataPenerima)
        jumlah_uang = float(input("Masukkan jumlah uang yang ingin ditransfer: "))

        pengirim = None
        penerima = None
        
        for data in rekeningNasabah:
            if data['PIN'] == dataPengirim:
                pengirim = data
            if data['PIN'] == dataPenerima:
                penerima = data

        if pengirim is None or penerima is None:
            print("PIN pengirim atau penerima tidak valid atau nasabah tidak terdaftar.")
            input("Tekan Enter untuk kembali...")
        else:
            if jumlah_uang < 0 or jumlah_uang > pengirim['Saldo']:
                print("Jumlah uang tidak valid atau saldo tidak mencukupi.")
                input("Tekan Enter untuk kembali...")
            else:
                pengirim['Saldo'] -= jumlah_uang
                penerima['Saldo'] += jumlah_uang
                simpan_ke_csv()
                print("Transfer uang berhasil.")
                waktuSekarang = datetime.now()
                waktu_invoice = waktuSekarang.strftime("%d-%m-%Y %H:%M:%S")
                print("Invoice Transfer:")
                print(f"Pengirim: {pengirim['Nama']}")
                print(f"Penerima: {penerima['Nama']}")
                print(f"Jumlah Uang: Rp {jumlah_uang:,.2f}".replace(",", "."))
                print(f"Saldo Pengirim: Rp {pengirim['Saldo']:,.2f}".replace(",", "."))
                print(f"Saldo Penerima: Rp {penerima['Saldo']:,.2f}".replace(",", "."))
                print(f"Detail Waktu: {waktu_invoice}")
                input("Tekan Enter untuk kembali...")
    except:
        print("Input tidak valid")

def tampilRekening():
    bersihkan_layar()
    tabel = PrettyTable(['Nama', 'Saldo'])
    for data in rekeningNasabah:
        tabel.add_row([data['Nama'], f"Rp {data['Saldo']:,.2f}".replace(",",".")])
    print(tabel)

def tampilRekening1():
    bersihkan_layar()
    PIN = pwinput.pwinput("Masukkan PIN Nasabah: ",mask='*')
    PIN = int(PIN)

    temukanNasabah = False

    for data in rekeningNasabah:
        if data['PIN'] == PIN:
            temukanNasabah = True
            tabel = PrettyTable(['Nama', 'Saldo'])
            tabel.add_row([data['Nama'], f"Rp {data['Saldo']:,.2f}".replace(",",".")])
            print(tabel)
            break
    
    if not temukanNasabah:
        print("PIN Salah atau nasabah tidak ditemukan.")
        input("Tekan Enter untuk kembali...")

def sortirSaldo():
    bersihkan_layar()
    rekeningNasabah.sort(key=lambda x: x['Saldo'], reverse=True)
    tampilRekening()
    print(f"{'-'*40:^40}")
    print(f"{'Saldo berhasil disortir.':^40}")
    print(f"{'-'*40:^40}")

def buatRekening():
    bersihkan_layar()
    print(f"{'-'*40:^40}")
    print(f"{'Buat Rekening Baru':^40}")
    print(f"{'-'*40:^40}")
    nama = input("Masukkan nama nasabah: ")
    pin = pwinput.pwinput("Buat PIN: ")
    pin = int(pin)
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

def cariNasabah():
    bersihkan_layar()
    print(f"{'-'*40:^40}")
    print(f"{'Cari Informasi Nasabah':^40}")
    print(f"{'-'*40:^40}")
    informasi = pwinput.pwinput("Masukkan PIN atau Nama nasabah yang ingin dicari: ")
    informasi = int(informasi)
    ditemukan = False

    for data in rekeningNasabah:
        if data['Nama'].lower() == informasi:
            ditemukan = True
            tabel = PrettyTable(['Nama', 'Saldo'])
            tabel.add_row([data['Nama'], f"Rp {data['Saldo']:,.2f}".replace(",", "."), data['PIN']])
            print(tabel)
            break
    
    if not ditemukan:
        print("Nasabah tidak ditemukan.")
    
    input("Tekan Enter untuk kembali...")

def perbaruiRekening():
    bersihkan_layar()
    print(f"{'-'*40:^40}")
    print(f"{'Perbarui Rekening':^40}")
    print(f"{'-'*40:^40}")
    try:
        PIN = pwinput.pwinput("Masukkan PIN nasabah yang ingin dirubah: ", mask='*')
        PIN = int(PIN)

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
            input("Tekan Enter untuk kembali ke menu admin...")
        else:
            print("PIN tidak valid atau nasabah tidak terdaftar.")

    except ValueError:
        print("Input Tidak Valid. Masukkan angka")
        input("Tekan Enter untuk kembali ke menu utama...")

def hapusRekening():
    bersihkan_layar()
    print(f"{'-'*40:^40}")
    print(f"{'Hapus Rekening':^40}")
    print(f"{'-'*40:^40}")
    PIN = pwinput.pwinput("Masukkan PIN Nasabah yang akan dihapus: ", mask='*')
    PIN = int(PIN)

    ditemukan = False
    for data in rekeningNasabah:
        if data['PIN'] == PIN:
            ditemukan = True
            rekeningNasabah.remove(data)
            print("Rekening nasabah telah berhasil dihapus.")
            simpan_ke_csv()
            break
    if not ditemukan:
        print("PIN Salah atau nasabah tidak terdaftar.")
    
    input("Tekan Enter untuk kembali ke menu addmin...")

def menuAdmin():
    while True:
        bersihkan_layar()
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
        print("8. Keluar dari program")
        print(f"{'-'*40:^40}")
        pilihan = int(input("Pilih Menu (1/2/3/4/5/6/7/8): "))

        if pilihan == 1:
            bersihkan_layar()
            tampilRekening()
            input("Tekan Enter untuk kembali ke beranda Admin..")
        if pilihan == 2:
            sortirSaldo()
        if pilihan == 3:
            buatRekening()
        if pilihan == 4:
            cariNasabah()
        if pilihan == 5:
            perbaruiRekening()
        if pilihan == 6:
            hapusRekening()
        if pilihan == 7:
            bersihkan_layar()
            menuUtama()
            return
        if pilihan == 8:
            bersihkan_layar()
            print(f"{'-'*40:^40}")
            print(f"{'Terima Kasih !':^40}")
            print(f"{'-'*40:^40}")
            break

def menuUtama():
    while True:
        try:
            bersihkan_layar()
            print(f"{'-'*40:^40}")
            print(f"{'Livin by Mandiri':^40}")
            print(f"{'-'*40:^40}")
            print("1. Admin")
            print("2. Nasabah")
            print("3. Keluar")
            print(f"{'-'*40:^40}")
            opsi = int(input("Pilih menu (1/2/3): "))

            if opsi == 1:
                print(f"{'-'*40:^40}")
                print(f"{'Selamat Datang Admin Mandiri.':^40}")
                print(f"{'-'*40:^40}")
                userAdmin = str(input("Masukkan username admin: "))
                passAdmin = pwinput.pwinput("Masukkan password admin: ")
                passAdmin = int(passAdmin)

                if userAdmin == dataAdmin['nama'] and passAdmin == dataAdmin['passAdmin']:
                    menuAdmin()

            if opsi == 2:
                while True:
                    print(f"{'-'*40:^40}")
                    print(f"{'Pilih menu nasabah':^40}")
                    print(f"{'-'*40:^40}")
                    print("1. Buat rekening baru")
                    print("2. Menabung")
                    print("3. Kirim uang")
                    print("4. Kembali ke beranda")
                    print("5. Keluar dari program")
                    print(f"{'-'*40:^40}")
                    pilihan = int(input("Pilih Menu (1/2/3/4/5/6): "))

                    if pilihan == 1:
                        print(f"{'-'*40:^40}")
                        print("Buat rekening hanya bisa di lakukan oleh Admin. Silahkan datang ke loket administrasi untuk melakukan pendaftaran.")
                        print(f"{'-'*40:^40}")
                        input("Tekan Enter untuk kembali ke Beranda...")
                    if pilihan == 2:
                        setorUang()
                    if pilihan == 3:
                        transferUang()
                    if pilihan == 4:
                        bersihkan_layar()
                        break
                    if pilihan == 5:
                        print(f"{'-'*40:^40}")
                        print(f"{'Terima Kasih !':^40}")
                        print(f"{'-'*40:^40}")
                        break

            if opsi == 3:
                print(f"{'-'*40:^40}")
                print(f"{'Terima Kasih !':^40}")
                print(f"{'-'*40:^40}")
                break
            continue
        except:
            print("Input Tidak Valid. Masukkan angka")
            input("Tekan Enter untuk kembali ke menu utama...")

menuUtama()
