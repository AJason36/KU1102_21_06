# Program Simulasi ATM
# Program ini akan menampilkan cara kerja sebuah mesin ATM
# Cara kerja yang ditampilkan program ini adalah:

# KAMUS
# Rek1, Rek2, Rek 3: Array [0..4] of str
# ListRek : matrix of string
# ongoing, atm_sim : bool
# end_sim : char

# Database berisi info setiap rekening (No Rek, Nama, Saldo, Status Blokir)
Rek1 = ["135165213270", "123456", "Farhan Nabil Suryono", "100000000", "eligible"]
Rek2 = ["135165213470", "234567", "Alexander Jason", "100000000", "eligible"]
Rek3 = ["135165214470", "987654", "Simbolon, Patrick Vyto P.", "100000000", "eligible"]
ListRek = [Rek1, Rek2, Rek3]


# Fungsi Sistem Utama ATM
def atm_main():
    # Memulai ATM dengan memasukkan rekening (Mensimulasikan proses ketika memasukkan kartu)

    # KAMUS LOKAL
    # rek_user : str

    # ALGORITMA
    global ongoing
    rek_user = input("\nMasukkan Rekening Anda: ")
    if user(rek_user):
        if auth(user(rek_user)):
            while user(rek_user)[4] == "eligible" and ongoing:
                menu(user(rek_user))
            print("\nTerima kasih telah menggunakan layanan kami.")
    else:
        print("Nomor Rekening tidak teridentifikasi.")


# Fungsi Menentukan Pengguna ATM
def user(a):
    # Mengecek apakah nomor rekening yang diinput valid dan mengambil info rekening

    # KAMUS LOKAL
    # i : int

    # ALGORITMA
    for i in range(len(ListRek)):
        if a == ListRek[i][0]:
            return ListRek[i]
    return False


# Fungsi Autentikasi
def auth(a):
    # Menentukan kebolehan melanjutkan dengan mengecek PIN

    # KAMUS LOKAL
    # j : int
    # pin : str

    # ALGORITMA
    if a[4] == "eligible":
        for j in range(3):
            pin = input("Masukkan PIN: ")
            if pin == a[1]:
                return True
            else:
                print("PIN yang dimasukkan salah.\n")
        print("Kesalahan memasukkan PIN telah melampaui batas.\nKartu akan diblokir.")
        a[4] = "ineligible"
        return False
    else:
        print("Kartu ini sedang terblokir.")
        return False


# Fungsi Tampilan Menu
def menu(a):
    # Menampilkan menu ATM

    # KAMUS LOKAL
    # opsi : char

    # ALGORITMA
    global ongoing
    print("\n\n" + 8*"=" + "MENU" + 8*"=")
    print("1. Penarikan Tunai")
    print("2. Informasi Saldo")
    print("3. Ganti PIN")
    print("4. Transfer")
    print("0. Keluar\n")

    opsi = input("Pilih opsi yang diinginkan: ")
    if opsi == '1':
        print("\n" + 3*"=" + "Penarikan Tunai" + 2*"=" + "\n")
        tariktunai(a)
    elif opsi == '2':
        print("\n" + 3*"=" + "Informasi Saldo" + 2*"=" + "\n")
        ceksaldo(a)
    elif opsi == '3':
        print("\n" + 6*"=" + "Ganti PIN" + 5*"=" + "\n")
        gantipin(a)
    elif opsi == '4':
        print("\n" + 6*"=" + "Transfer" + 6*"=" + "\n")
        transfer(a)
    else:
        ongoing = False


# Fungsi Menarik Uang Tunai
def tariktunai(a):
    # Mensimulasikan proses ketika menarik uang tunai yaitu mengurangi saldo pengguna sebanyak yang ditarik

    # KAMUS LOKAL
    # opsi : char
    # sisa_saldo, nom : int

    # ALGORITMA
    print("1. 250.000")
    print("2. 500.000")
    print("3. 1.000.000")
    print("4. 2.000.000")
    print("5. Nominal Lainnya")
    opsi = input("Pilih opsi yang diinginkan: ")
    if opsi == '1' and int(a[3]) >= 250000:
        print("\nMelakukan penarikan tunai...")
        sisa_saldo = int(a[3]) - 250000
        a[3] = str(sisa_saldo)
        print("Sisa saldo anda: " + "Rp {:,}" .format(int(a[3])).replace(",", ".") + ",00")
        ceklanjut()
    elif opsi == '2' and int(a[3]) >= 500000:
        print("\nMelakukan penarikan tunai...")
        sisa_saldo = int(a[3]) - 500000
        a[3] = str(sisa_saldo)
        print("Sisa saldo anda: " + "Rp {:,}" .format(int(a[3])).replace(",", ".") + ",00")
        ceklanjut()
    elif opsi == '3' and int(a[3]) >= 1000000:
        print("\nMelakukan penarikan tunai...")
        sisa_saldo = int(a[3]) - 1000000
        a[3] = str(sisa_saldo)
        print("Sisa saldo anda: " + "Rp {:,}" .format(int(a[3])).replace(",", ".") + ",00")
        ceklanjut()
    elif opsi == '4' and int(a[3]) >= 2000000:
        print("\nMelakukan penarikan tunai...")
        sisa_saldo = int(a[3]) - 2000000
        a[3] = str(sisa_saldo)
        print("Sisa saldo anda: " + "Rp {:,}" .format(int(a[3])).replace(",", ".") + ",00")
        ceklanjut()
    elif opsi == '5':
        nom = int(input("\nMasukkan nominal yang mau ditarik (Rp): "))
        while nom % 50000 != 0:
            print("Penarikan tunai harus dalam kelipatan Rp 50.000,00\n")
            nom = int(input("Masukkan nominal yang mau ditarik (Rp): "))
        if int(a[3]) >= nom:
            print("\nMelakukan penarikan tunai...")
            sisa_saldo = int(a[3]) - nom
            a[3] = str(sisa_saldo)
            print("Sisa saldo anda: " + "Rp {:,}" .format(int(a[3])).replace(",", ".") + ",00")
            ceklanjut()
        else:
            print("Maaf, saldo anda tidak mencukupi.")
            ceklanjut()
    else:
        print("Maaf, saldo anda tidak mencukupi.")
        ceklanjut()


# Fungsi Mengecek Saldo
def ceksaldo(a):
    # Mengecek saldo pengguna

    # KAMUS LOKAL

    # ALGORITMA
    print("Saldo anda sebanyak: " + "Rp {:,}" .format(int(a[3])).replace(",", ".") + ",00")
    ceklanjut()


# Fungsi Ganti PIN
def gantipin(a):
    # Mengganti PIN pengguna

    # KAMUS LOKAL
    # opin, npin, cnpin : str
    # ulang : char

    # ALGORITMA
    global ongoing
    opin = input("Masukkan PIN lama: ")
    if opin == a[1]:
        npin = input("Masukkan PIN baru: ")
        if len(npin) != 6:
            print("PIN yang dimasukkan harus 6 digit.\n")
            ulang = input("Apakah mau mengulang?(Y/N): ")
            if ulang == 'Y' or ulang == 'y':
                gantipin(a)
            elif ulang == 'N' or ulang == 'n':
                ceklanjut()
            else:
                print("\nMasukkan Y untuk mengulang atau N untuk membatalkan.")
        else:
            cnpin = input("Konfirmasi PIN baru: ")
            if npin != cnpin:
                print("Konfirmasi PIN baru gagal.\n")
                ulang = input("Apakah mau mengulang?(Y/N): ")
                if ulang == 'Y' or ulang == 'y':
                    gantipin(a)
                elif ulang == 'N' or ulang == 'n':
                    ceklanjut()
                else:
                    print("\nMasukkan Y untuk mengulang atau N untuk membatalkan.")
            else:
                a[1] = str(npin)
                print("Penggantian PIN berhasil")
                ceklanjut()
    else:
        print("\nPIN lama yang anda masukkan salah.\nTransaksi kami tutup.")
        ongoing = False


# Fungsi Transfer Uang
def transfer(a):
    # Mensimulasi proses transfer antar rekening

    # KAMUS LOKAL
    # rek_user, r : str
    # nom, saldo_tujuan, sisa_saldo : int
    # lanjut : char

    # ALGORITMA
    rek_user = a[0]

    def rektujuan(n):
        # Mengambil info dari rekening tujuan

        # KAMUS LOKAL
        # i : int

        # ALGORITMA
        for i in range(len(ListRek)):
            if n == ListRek[i][0]:
                return ListRek[i]
        return False
    r = input("Masukkan rekening tujuan: ")
    if r == rek_user:
        print("Transfer tidak bisa dilakukan.")
        ceklanjut()
    else:
        if rektujuan(r):
            nom = int(input("Masukkan nominal yang ingin ditransfer (Rp): "))
            print("\nTujuan: " + str(r))
            print("Nama: " + rektujuan(r)[2])
            print("Jumlah: " + "Rp {:,}" .format(nom).replace(",", ".") + ",00")
            lanjut = input("Lakukan transfer (Y/N)? ")
            if int(a[3]) >= nom and (lanjut == 'Y' or lanjut == 'y'):
                saldo_tujuan = int(rektujuan(r)[3]) + nom
                rektujuan(r)[3] = str(saldo_tujuan)
                print("\nTransfer berhasil.")

                sisa_saldo = int(a[3]) - nom
                a[3] = str(sisa_saldo)
                print("Sisa saldo anda: " + "Rp {:,}" .format(int(a[3])).replace(",", ".") + ",00")
                ceklanjut()
            elif int(a[3]) < nom and (lanjut == 'Y' or lanjut == 'y'):
                print("\nMaaf, saldo anda tidak mencukupi.")
                ceklanjut()
            elif lanjut == 'N' or lanjut == 'n':
                print("\nTransfer dibatalkan.")
                ceklanjut()
            else:
                print("\nMasukkan Y untuk lanjut atau N untuk membatalkan.")

        else:
            print("Nomor rekening tujuan tidak teridentifikasi.")
            ceklanjut()


# Fungsi Mengecek Keinginan Melanjutkan Transaksi
def ceklanjut():
    # Mengecek apakah pengguna ingin melanjutkan transaksi

    # KAMUS LOKAL
    # lanjut : char

    # ALGORITMA
    global ongoing
    lanjut = input("\nLanjut transaksi (Y/N)?: ")
    if lanjut == 'Y' or lanjut == 'y':
        ongoing = True
    elif lanjut == 'N' or lanjut == 'n':
        ongoing = False
    else:
        print("\nMasukkan Y untuk lanjut atau N untuk berhenti.")
        ceklanjut()


# Sistem Utama Simulasi
ongoing = True
print("Program ATM\n")
atm_sim = True
while atm_sim:
    atm_main()
    end_sim = input("\nAkhiri simulasi?\nMasukkan Y untuk melanjutkan.\nMasukkan apapun untuk mengakhiri.\n")
    if end_sim == 'Y' or end_sim == 'y':
        ongoing = True
    else:
        atm_sim = False
print("\nSimulasi telah diakhiri")
