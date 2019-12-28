def inputan():
    from model.daftar_nilai import tambah_data
    while (True):
        nim = input("Nim: ")
        if nim == '':
            print('Masukkan Nim')
        else:
            break
    while (True):
        try:
            nama = input("Nama: ")
            if nama == '':
                print('Masukkan NAMA anda')
        except ValueError:
            print('Nama tidak diisi!! silahkan Masukkan Nama anda kembali')
        else:
            break
    while (True):
        try:
            tugas = int(input("TUGAS: "))
            if tugas == '':
                print('Masukan Nilai Tugas')
        except ValueError:
            print('Nilai Tidak diisi!! silahkan Masukkan Nilai Tugas Kembali')
        else:
            break
    while (True):
        try:
            uts = int(input("UTS: "))
            if uts == '':
                print('Masukkan Nilai Uts')
        except ValueError:
            print('Nilai Tidak diisi!! silahkan Masukkan Nilai Uts kembali')
        else:
            break
    while (True):
        try:
            uas = int(input("UAS: "))
            if uas == '':
                print('Masukkan Nilai Uas')
        except ValueError:
            print('Nilai Tidak diisi!! silahkan Masukkan Nilai Uas kembali')
        else:
            break
    tambah_data(nama, nim, tugas, uts, uas)
    print("\n    (A)dd       (E)dit      (D)elete     (S)earch      (L)ist     (Q)uit   ")

def edit():
    from model.daftar_nilai import edit_data
    edit_data(nim=input("Masukan Nim anda: "))

def delete():
    from model.daftar_nilai import delete_data
    delete_data(nim=input("Masukan Nim anda Untuk Menghapus Data yg tersedia: "))
    print("\n    (A)dd       (E)dit      (D)elete     (S)earch      (L)ist     (Q)uit   ")


def nyari():
    from model.daftar_nilai import cari_data
    cari_data(nim=input("Masukan Nim untuk Mencari Data: "))