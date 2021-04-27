#import os
#import sys
#import math
#import time 
#import argparse
 
#from functionsTubes import *

# F14
#def load_data():

    # Membaca argument pada commandline saat mengeksekusi file
#    try:
#        cwd = os.getcwd()
#        os.chdir(sys.argv[1])

        # load .csv dari folder
#        global user_matrix
#        global consumable_matrix
#        global consumable_history_matrix
#        global gadget_matrix
#        global gadget_borrow_history_matrix
#        global gadget_return_history_matrix

#        user_matrix = csv_to_matrix("user.csv")
#        consumable_matrix = csv_to_matrix("consumable.csv")
#        gadget_matrix = csv_to_matrix("gadget.csv")
#        consumable_history_matrix = csv_to_matrix("consumable_history.csv")
#        gadget_borrow_history_matrix = csv_to_matrix("gadget_borrow_history.csv")
#        gadget_return_history_matrix = csv_to_matrix("gadget_return_history.csv")

#    except IndexError:
#        print("Tidak ada nama Folder yang diberikan!")

#    os.chdir(cwd)

# F15
#def save_data(folder):
#    if not os.path.exists(folder):
#        os.makedirs(folder)

#    os.chdir(folder)
#    user_matrix_string = data_matrix_to_string(user_matrix)
#    consumable_matrix_string = data_matrix_to_string(consumable_matrix)
#    consumable_history_matrix_string = data_matrix_to_string(consumable_history_matrix)
#    gadget_matrix_string = data_matrix_to_string(gadget_matrix)
#    gadget_borrow_history_matrix_string = data_matrix_to_string(gadget_borrow_history_matrix)
#    gadget_return_history_matrix_string = data_matrix_to_string(gadget_return_history_matrix)
 
#    write_data(user_matrix_string,"user.csv")
#    write_data(consumable_matrix_string,"consumable.csv")
#    write_data(consumable_history_matrix_string,"consumable_history.csv")
#    write_data(gadget_matrix_string,"gadget.csv")
#    write_data(gadget_borrow_history_matrix_string,"gadget_borrow_history.csv")
#    write_data(gadget_return_history_matrix_string,"gadget_return_history.csv")

#    print("Semua data tersimpan!")

# F05
def tambahitem():
    iditem = str(input("Masukkan ID              : "))

    cekid = list(iditem)
    validdata = 0

    # Pengecekan ID
    if cekid[0] == "G":
        for i in range(len(gadget_matrix)):
            if gadget_matrix[i][0] == iditem:
                validdata += 1
    elif cekid[0] == "C":
        for i in range(len(consumable_matrix)):
            if consumable_matrix[i][0] == iditem:
                validdata += 1
    elif (cekid[0] != "C" and cekid[0] != "G"):
        validdata = 1

    # validdata = 0 berarti ID belum dipakai dan bisa ditambahkan
    if validdata == 0:
        # Gadget
        if cekid[0] == "G":
            namaitem = str(input("Masukkan nama            : "))
            descitem = str(input("Masukkan deskripsi       : "))
            jumlahitem = int(input("Masukkan jumlah          : "))
            rarityitem = str(input("Masukkan rarity          : "))

            if (rarityitem == "C" or rarityitem == "B" or rarityitem == "A" or rarityitem == "S"):
                tahunitem = int(input("Masukkan tahun ditemukan : "))
                itemgdata = [iditem, namaitem, descitem, jumlahitem, rarityitem, tahunitem]

                gadget_matrix.append(itemgdata)

                print()
                print("Item telah berhasil ditambahkan ke database.")

                return gadget_matrix

            else:
                print()
                print("Input rarity tidak valid!")

        # Consumable
        elif cekid[0] == "C":
            namaitem = str(input("Masukkan nama            : "))
            descitem = str(input("Masukkan deskripsi       : "))
            jumlahitem = int(input("Masukkan jumlah          : "))
            rarityitem = str(input("Masukkan rarity          : "))

            if (rarityitem == "C" or rarityitem == "B" or rarityitem == "A" or rarityitem == "S"):
                itemdata = [iditem, namaitem, descitem, jumlahitem, rarityitem]

                consumable_matrix.append(itemdata)

                print()
                print("Item telah berhasil ditambahkan ke database.")

                return consumable_matrix

            else:
                print()
                print("Input rarity tidak valid!")

    # validdata = 1 berarti sudah ada ID tersebut atau ID tidak valid
    else:
        if cekid[0] == "C" or cekid[0] == "G":
            print("Gagal menambahkan item karena ID sudah ada!")
        else:
            print("Gagal menambahkan item karena ID tidak valid.")

# F06
def hapusitem():
    hapusid = input("Masukkan ID: ")
    iditem = list(hapusid)

    # Deklarasi awal
    valid = 0
    # Gadget
    if iditem[0] == "G":
        for i in range(len(gadget_matrix)):
            if gadget_matrix[i][0] == hapusid:
                valid += 1
                yesno = input("Apakah Anda yakin ingin menghapus " + str(gadget_matrix[i][1]) + " (Y/N)?: ")

                if yesno == "Y":
                    gadget_matrix.remove(gadget_matrix[i])
                    print()
                    print("Item telah berhasil dihapus dari database.")
                elif yesno == "N":
                    print("Item tidak dihapus dari database.")
                else:
                    print("Tidak valid!")

            # Tidak ada ID tersebut di database
            else:
                valid += 0

        if valid == 0:
            print("Tidak ada item dengan ID tersebut!")
        else:
            return gadget_matrix

    # Consumable
    elif iditem[0] == "C":
        for i in range(len(consumable_matrix)):
            if consumable_matrix[i][0] == hapusid:
                valid += 1
                yesno = input("Apakah Anda yakin ingin menghapus " + str(consumable_matrix[i][1]) + " (Y/N)?: ")

                if yesno == "Y":
                    consumable_matrix.remove(consumable_matrix[i])
                    print()
                    print("Item telah berhasil dihapus dari database.")
                elif yesno == "N":
                    print("Item tidak dihapus dari database.")
                else:
                    print("Tidak valid!")

            # Tidak ada ID tersebut di database
            else:
                valid += 0

        if valid == 0:
            print("Tidak ada item dengan ID tersebut!")
        else:
            return consumable_matrix

    # ID =/= C atau G
    else:
        print("ID item tidak valid!")

# F07
def ubahjumlah():
    idnya = str(input("Masukkan ID                              : "))
    iditem = list(idnya)

    #Deklarasi awal
    ada = 0

    # Gadget
    if iditem[0] == "G":
        for i in range(len(gadget_matrix)):
            if gadget_matrix[i][0] == idnya:
                ada += 1
                ubah = int(input("Masukkan jumlah barang yang ditambahkan  : "))
                # Pengecekan jika stok diubah apakah valid
                cekstok = int(gadget_matrix[i][3]) + ubah

                if cekstok <= 0:
                    print(str(abs(ubah)) + " " + str(gadget_matrix[i][1]) + " gagal dibuang karena stok kurang. Stok sekarang: " + str(gadget_matrix[i][3]))
                else:
                    if ubah > 0:
                        gadget_matrix[i][3] = int(gadget_matrix[i][3]) + ubah
                        print(str(ubah) + " " + str(gadget_matrix[i][1]) + " berhasil ditambahkan. Stok sekarang: " + str(gadget_matrix[i][3]))
                    elif ubah < 0:
                        gadget_matrix[i][3] = int(gadget_matrix[i][3]) + ubah
                        print(str(abs(ubah)) + " " + str(gadget_matrix[i][1]) + " berhasil dibuang. Stok sekarang: " + str(gadget_matrix[i][3]))
                    else:
                        # Nilai ubah = 0
                        print("Tidak ada perubahan jumlah item.")

            else:
                ada += 0

        # ada = 0 tidak ada ID tersebut dalam data
        if ada == 0:
            print("Tidak ada item dengan ID tersebut!")
        else:
            return gadget_matrix
    
    #Consumable 
    elif iditem[0] == "C":
        for i in range(len(consumable_matrix)):
            if consumable_matrix[i][0] == idnya:
                ada += 1
                ubah = int(input("Masukkan jumlah barang yang ditambahkan  : "))
                # Pengecekan jika stok diubah apakah valid
                cekstok = int(consumable_matrix[i][3]) + ubah

                if cekstok <= 0:
                    print(str(abs(ubah)) + " " + str(consumable_matrix[i][1]) + " gagal dibuang karena stok kurang. Stok sekarang: " + str(consumable_matrix[i][3]))
                else:
                    if ubah > 0:
                        consumable_matrix[i][3] = int(consumable_matrix[i][3]) + ubah
                        print(str(ubah) + " " + str(consumable_matrix[i][1]) + " berhasil ditambahkan. Stok sekarang: " + str(consumable_matrix[i][3]))
                    elif ubah < 0:
                        consumable_matrix[i][3] = int(consumable_matrix[i][3]) + ubah
                        print(str(abs(ubah)) + " " + str(consumable_matrix[i][1]) + " berhasil dibuang. Stok sekarang: " + str(consumable_matrix[i][3]))
                    else:
                        # Nilai ubah = 0
                        print("Tidak ada perubahan jumlah item.")

            else:
                ada += 0

        # ada = 0 tidak ada ID tersebut dalam data
        if ada == 0:
            print("Tidak ada item dengan ID tersebut!")
        else:
            return consumable_matrix

    # ID =/= C atau G
    else:
        print("ID item tidak valid!")

#load_data()
#run = True

#while run: 
#    action = str(input("mau ngapain?? "))

#    if action == "save":
#        tempat = str(input("Masukkan nama folder penyimpanan: "))
#        save_data(tempat)
#    elif action == "exit":
#        run = False
#    elif action == "tambah item":
#        tambahitem()
#    elif action == "hapus item":
#        hapusitem()
#    elif action == "ubah jumlah":
#        ubahjumlah()