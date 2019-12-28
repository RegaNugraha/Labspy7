from view.view_nilai import nyari,cetak
from view.input_nilai import inputan,edit,delete

while True:

    c = input("\nPilih Opsi: ")

    # KELUA PROGRAM
    if c.lower() == 'q':
        print("Pemograman Module&Paket/Package")
        ext = input("\nPress ENTER to exit")
        if ext == '':
            break
        else:
            break

    # TAMPILKAN LIST DATA
    elif c.lower() == 'l':
        cetak()

    # MENAMBAH DATA
    elif c.lower() == 'a':
        inputan()

    # EDIT DATA
    elif c.lower() == 'e':
        edit()

    # MENCARI DATA
    elif c.lower() == 's':
        nyari()

    # HAPUS DATA
    elif c.lower() == 'd':
        delete()

    else:
        print("Pilih data yang tersedia")