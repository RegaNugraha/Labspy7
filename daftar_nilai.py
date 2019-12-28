data = {}


def tambah_data(nama,nim,tugas,uts,uas):
    akhir = round((float(tugas) *30/100) + (float(uts) *35/100) + (float(uas) *35/100), 2)
    data[nim] = nama,tugas,uts,uas,akhir


def edit_data(nim):
    if nim in data.keys():
        del data[nim]
        print("\n===Masukan Pembaruan Data===")
        from view.input_nilai import inputan
        inputan()
    else:
        print("==========================")
        print("| Data {0} tidak ditemukan |".format(nim))
        print("==========================")
        print("    (A)dd       (E)dit      (D)elete     (S)earch      (L)ist     (Q)uit   ")


def cari_data(nim):
    if nim in data.keys():
        print("\n|===================================================================|")
        print("|      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
        print("|===================================================================|")
        print("| {0:15} | {1:16} | {2:5} | {3:5} | {4:5} | {5:5} |".format(nim, data[nim][1], data[nim][2],data[nim][3],data[nim][4], data[nim][5]))
        print("|===================================================================|")
    else:
        print("===========================")
        print("| Data {0} tidak ditemukan |".format(nim))
        print("===========================")


def delete_data(nim):
    if nim in data.keys():
        del data[nim]
        print('nama berhasil di hapus')
        return True
    else:
        print("===========================")
        print("| Data {0} tidak ditemukan |".format(nim))
        print("===========================")
        return False