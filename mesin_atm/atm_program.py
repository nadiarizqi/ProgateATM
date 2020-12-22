import datetime
import random
import sys

from customer import Customer
from atm_card import ATMCard

nasabah = Customer(id = 1, card = ATMCard())

menus = [
  "Cek Saldo",
  "Debet",
  "Simpan",
  "Ganti Pin",
  "Keluar"
]

while True:
    trial = 0

    id = int(input("Masukan pin Anda: "))

    while id != nasabah.get_custPin():
      trial += 1
      if trial > 2:
        print("Error. Silahkan ambil kartu dan coba lagi.")
        exit()

      id = int(input("Pin Anda salah. Silahkan masukan lagi: "))
  
    while True:
        print("Selamat Datang")
        panjang_menu = len(menus)
        for index in range(panjang_menu):
          print(str(index + 1) + '. ' + menus[index])

        menu_dipilih = int(input("Pilih menu: "))

        if menu_dipilih == 1:
          print(nasabah.get_custBalance())
        elif menu_dipilih == 2:
          nominal = int(input("Nominal yang ingin diambil:"))
          if nominal > 0 and nominal < nasabah.get_custBalance():
            nasabah.withdraw_balance(nominal)
            print("Saldo akhir: " + str(nasabah.get_custBalance()))
        elif menu_dipilih == 3:
          nominal = int(input("Nominal yang ingin dideposit:"))
          if nominal > 0:
            nasabah.deposit_balance(nominal)
            print("Saldo akhir: " + str(nasabah.get_custBalance()))
        elif menu_dipilih == 4:
          new_pin = int(input("Masukkan pin baru:"))
          if new_pin == nasabah.get_custPin():
            print("Mengubah pin gagal: Pin sama")
          elif new_pin < 0:
            print("Mengubah pin gagal: Pin invalid")
          else:
            nasabah.set_custPin(new_pin)
            print("Pin berhasil diubah")
        elif menu_dipilih == 5:
          resi = random.randint(100000, 1000000)
          tgl_hari_ini = datetime.date.today()
          sisa_saldo = nasabah.get_custBalance()
          print('|  Resi  |     Tgl    | Saldo |')
          print('-------------------------------')
          print('|', resi, '|', tgl_hari_ini, '|', sisa_saldo, '|')
          exit()
        else:
          print('Tidak diketahui')
    