# Daftar Isi spesifikasi yang udah:
# F01
# F02
# F03
# F04
# F05
# F06
# F07
# F08
# F09
# F10
# F11
# F12
# F13
# F14
# F15
# F16
# F17

import os
import sys
import math
import time 
import argparse
import datetime

# ----------------------------------------------------------------------------- #### FUNGSI PEMBANTU ##### ----------------------------------------------------------------------------- 

# .split substitute untuk .csv
def csvSplitter(x):
    li = []
    # Hitung berapa koma
    for _ in range(x.count(",") + 1):
        string = ""
        # memisah koma dengan string
        for j in x:
            if j == ",":
                break
            string += j
        # reassign x dari koma 
        x = x[len(string) + 1 : len(x)]
        # menambah string pada li
        li.append(string)
    # return list
    return li

# konversi lagi matrix ke string untuk diwrite ke .csv
def data_matrix_to_string(data_matrix):
    data_string = ""
    for arr_data in data_matrix:
        all_string = [str(var) for var in arr_data]
        data_string += ",".join(all_string)
        data_string += "\n"
    return data_string

# konversi string .csv menjadi array dan membersihkan
def line_to_data(x):
    raw_array_of_data = csvSplitter(x)
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

# konvert data string menjadi tipe yang sesuai 
def data_to_values(x,data):
    # ganti ke data type sesuai kebutuhan, ini cuman placeholder aja 
    arr_copy = data
    if x == "user.csv":
        for i in range(6):
            if i == 0:
                arr_copy[i] = str(arr_copy[i])
        return arr_copy
    elif x == "consumable.csv":
        for i in range(5):
            if i == 0:
                arr_copy[i] = str(arr_copy[i])
            elif i == 3:
                arr_copy[i] = int(arr_copy[i])
            elif i == 4:
                arr_copy[i] = str(arr_copy[i])
        return arr_copy
    elif x == "gadget.csv":
        for i in range(6):
            if i == 0:
                arr_copy[i] = str(arr_copy[i])
            elif i == 3:
                arr_copy[i] = int(arr_copy[i])
            elif i == 5:
                arr_copy[i] = int(arr_copy[i])
        return arr_copy
    elif x == "consumable_history.csv":
        for i in range(5):
            if i == 0:
                arr_copy[i] = str(arr_copy[i])
            elif i == 1:
                arr_copy[i] = str(arr_copy[i])
            elif i == 2:
                arr_copy[i] = str(arr_copy[i])
            elif i == 4:
                arr_copy[i] = int(arr_copy[i])
        return arr_copy
    elif x == "gadget_borrow_history.csv":
        for i in range(6):
            if i == 0:
                arr_copy[i] = str(arr_copy[i])
            elif i == 1:
                arr_copy[i] = str(arr_copy[i])
            elif i == 4:
                arr_copy[i] = int(arr_copy[i])
        return arr_copy
    elif x == "gadget_return_history.csv":
        for i in range(4):
            if i == 0:
                arr_copy[i] = str(arr_copy[i])
            elif i == 1:
                arr_copy[i] = str(arr_copy[i])
        return arr_copy


# fungsi penyatu
def csv_to_matrix(name):
    f = open(name, "r", encoding='utf8')
    f_lines = f.readlines()
    f.close()
    f_lines_clean = [line.replace("\n", "") for line in f_lines]

    f_header = f_lines_clean.pop(0)
    f_header_Cleaned = line_to_data(f_header)

    f_matrix = []
    f_matrix.append(f_header_Cleaned)
    for line in f_lines_clean:
        dataArray = line_to_data(line)
        dataArrayConverted = data_to_values(name,dataArray) 
        f_matrix.append(dataArrayConverted)

    return f_matrix

# fungsi write data
def write_data(string,name):
        fNew = open(name, "w", encoding="utf-8")
        fNew.write(string)




waktu = datetime.date.today()
tanggal = waktu.strftime("%d/%m/%Y")


# ----------------------------------------------------------------------------- #### FUNGSI SPESIFIKASI ##### ----------------------------------------------------------------------------- 

# -----------------------------------------------------------------------------  F01 Register -----------------------------------------------------------------------------  
def register():
    noID = len(user_matrix)
    print("No. ID kamu adalah ", noID)
    notavail = 0

    nama = str(input("Masukkan nama      : "))
    username = str(input("Masukkan username  : "))

    for i in range(len(user_matrix)):
        if username == user_matrix[i][1]:
            notavail += 1
        else:
            notavail += 0
        
    if notavail == 0:
        password = my_encrypt(username, str(input("Masukkan password  : ")))
        alamat = str(input("Masukkan alamat    : "))

        array = [noID,username,nama.title(),alamat,password,"user"]

        user_matrix.append(array)

        print("User", username, "telah berhasil register ke dalam Kantong Ajaib.")
        return user_matrix

    else:
        print("Gagal register karena username", username, "telah ada dalam database.")

# ----------------------------------------------------------------------------- F02 Login ----------------------------------------------------------------------------- 
def login():
    
    username = str(input("Masukkan username: "))
    
    for i in range(len(user_matrix)):
        if user_matrix[i][1] == username:
            password = str(input("Masukkan password: "))
            if user_matrix[i][4] == my_encrypt(username, password):
                #ID user buat F08-F10
                global active_user
                global nama_user
                active_user = user_matrix[i][0]
                nama_user = user_matrix[i][2]
                print()
                print("Halo, " + username + "! Selamat datang di Kantong Ajaib.")
                
                if user_matrix[i][5] == "admin":
                    print("Anda punya admin akses!")
                    return("Admin")
                else:
                    return("User")

            else:
                print("Password salah!")
                return ("Not logged in")

    print("Username tidak ditemukan!")
    return ("Not logged in")

# ----------------------------------------------------------------------------- F03 Cari Gadget Berdasarkan Rarity ----------------------------------------------------------------------------- 
def cariGadgetRarity():
    rarity = str(input("Masukkan rarity: "))
    # Membuat list semua rarity yang ada
    rarityList = []

    for i in range(1,len(gadget_matrix)):
        rarityList.append(gadget_matrix[i][4])

    # Cek validitas rarity
    if rarity == "A" or rarity == "a" or rarity == "C" or rarity == "c" or rarity == "b" or rarity == "B" or rarity == "S" or rarity == "s":
        print("\nHasil pencarian: \n")
        for i in range(1, len(gadget_matrix)):
            if gadget_matrix[i][4].lower() == rarity.lower():
                print("Nama            :", gadget_matrix[i][1])
                print("Deskripsi       :", gadget_matrix[i][2])
                print("Jumlah          :", gadget_matrix[i][3])
                print("Rarity          :", gadget_matrix[i][4])
                print("Tahun Ditemukan :", gadget_matrix[i][5], "\n")

        if rarity.lower() and rarity.upper() not in rarityList:
            print("Tidak ada gadget yang ditemukan\n")

    else: 
        print("Rarity tidak valid! (S, A, B, C)\n")

# ----------------------------------------------------------------------------- F04 Cari Gadget Berdasarkan tahun ditemukan ----------------------------------------------------------------------------- 
def cariGadgetTahun():
    tahun = int(input("Masukkan tahun: "))
    kategori = str(input("Masukkan kategori: "))

    if kategori == ">" or kategori == "<" or kategori == "<=" or kategori == ">=" or kategori == "=":
        tahunList = []
        # Membuat list semua tahun yang ada

        for i in range(1, len(gadget_matrix)):
            tahunList.append(gadget_matrix[i][5])
        # Membuat list tahun yang memenuhi kriteria
        listMemenuhi = []
        if kategori == "=":

            for i in range(1, len(gadget_matrix)):
                if tahun == gadget_matrix[i][5]:
                    print("Nama            :", gadget_matrix[i][1])
                    print("Deskripsi       :", gadget_matrix[i][2])
                    print("Jumlah          :", gadget_matrix[i][3])
                    print("Rarity          :", gadget_matrix[i][4])
                    print("Tahun Ditemukan :", gadget_matrix[i][5], "\n")
                    listMemenuhi.append(gadget_matrix[i][5])

            if not listMemenuhi:
                print("Tidak ada gadget yang ditemukan\n")

        elif kategori == ">":

            for i in range(1, len(gadget_matrix)):
                if gadget_matrix[i][5] > tahun:
                    print("Nama            :", gadget_matrix[i][1])
                    print("Deskripsi       :", gadget_matrix[i][2])
                    print("Jumlah          :", gadget_matrix[i][3])
                    print("Rarity          :", gadget_matrix[i][4])
                    print("Tahun Ditemukan :", gadget_matrix[i][5], "\n")
                    listMemenuhi.append(gadget_matrix[i][5])

            if not listMemenuhi:
                print("Tidak ada gadget yang ditemukan\n")

        elif kategori == ">=":

            for i in range(1, len(gadget_matrix)):
                if gadget_matrix[i][5] >= tahun:
                    print("Nama            :", gadget_matrix[i][1])
                    print("Deskripsi       :", gadget_matrix[i][2])
                    print("Jumlah          :", gadget_matrix[i][3])
                    print("Rarity          :", gadget_matrix[i][4])
                    print("Tahun Ditemukan :", gadget_matrix[i][5], "\n")
                    listMemenuhi.append(gadget_matrix[i][5])

            if not listMemenuhi:
                print("Tidak ada gadget yang ditemukan\n")

        elif kategori == "<":

            for i in range(1, len(gadget_matrix)):
                if gadget_matrix[i][5] < tahun:
                    print("Nama            :", gadget_matrix[i][1])
                    print("Deskripsi       :", gadget_matrix[i][2])
                    print("Jumlah          :", gadget_matrix[i][3])
                    print("Rarity          :", gadget_matrix[i][4])
                    print("Tahun Ditemukan :", gadget_matrix[i][5], "\n")
                    listMemenuhi.append(gadget_matrix[i][5])

            if not listMemenuhi:
                print("Tidak ada gadget yang ditemukan\n")

        elif kategori == "<=":

            for i in range(1, len(gadget_matrix)):
                if gadget_matrix[i][5] <= tahun:
                    print("Nama            :", gadget_matrix[i][1])
                    print("Deskripsi       :", gadget_matrix[i][2])
                    print("Jumlah          :", gadget_matrix[i][3])
                    print("Rarity          :", gadget_matrix[i][4])
                    print("Tahun Ditemukan :", gadget_matrix[i][5], "\n")
                    listMemenuhi.append(gadget_matrix[i][5])

            if not listMemenuhi:
                print("Tidak ada gadget yang ditemukan\n")

    

    else:
        print("Kategori tidak valid! (=, <, >, <=, >=)")

# ----------------------------------------------------------------------------- F05 Tambah Item ----------------------------------------------------------------------------- 
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

# ----------------------------------------------------------------------------- F06 Hapus Item ----------------------------------------------------------------------------- 
def hapusitem():
    hapusid = input("Masukkan ID: ")
    iditem = list(hapusid)

    # Deklarasi awal
    valid = 0
    # Gadget
    if iditem[0] == "G":
        for i in range(len(gadget_borrow_history_matrix)):
            if (hapusid == gadget_borrow_history_matrix[i][2]):
                print("Tidak bisa dihapus karena masih ada yang meminjam")
                break
        else:
            for i in range(len(gadget_matrix)):
                if gadget_matrix[i][0] == hapusid:
                    valid += 1
                    yesno = input("Apakah Anda yakin ingin menghapus " + str(gadget_matrix[i][1]) + " (Y/N)?: ")

                    if yesno == "Y":
                        gadget_matrix.remove(gadget_matrix[i])
                        print()
                        print("Item telah berhasil dihapus dari database.")
                        break
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
                    break
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

# ----------------------------------------------------------------------------- F07 Ubah Jumlah Item ----------------------------------------------------------------------------- 
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

# ----------------------------------------------------------------------------- F08 Pinjam Gadget ----------------------------------------------------------------------------- 
def pinjam_gadget():
    id = input("Masukkan ID item : ")
    indeks = 0
    #Kita cari indeks buat diubah jumlahnya
    for i in range (len(gadget_matrix)):
        if (id == gadget_matrix[i][0]):
            indeks = i
            break
        
    if (indeks != 0):
        for i in range (len(gadget_borrow_history_matrix)):
            if (active_user == gadget_borrow_history_matrix[i][1] and id == gadget_borrow_history_matrix[i][2]):
                print("Anda sudah pernah meminjam gadget ini")
                break
          
        else:    
            print("Stok yang tersedia :", gadget_matrix[indeks][3]) 
            if (gadget_matrix[indeks][3] == 0):
                print("Maaf, gadget sedang tidak tersedia")
            else:             
                jumlah = int(input("Jumlah peminjaman : "))
                #Karena udah tau indeksnya, kita bisa ngambil dari stok gudang berapa yang si user mau                    
                if (1 <= jumlah <= gadget_matrix[indeks][3]):
                    gadget_matrix[indeks][3] = gadget_matrix[indeks][3] - jumlah
                    print("Item", gadget_matrix[indeks][1], "sebanyak", str(jumlah),"telah dipinjam." )
                    stok_user = jumlah
                    #Data buat masuk history
                    global pinjam_history
                    pinjam_history = [int(gadget_borrow_history_matrix[-1][0])+1,active_user, id, tanggal, jumlah, stok_user]
                elif (jumlah <= 0):
                    print("Jumlah harus lebih dari 0")
                else:
                    print("Jumlah peminjaman terlalu banyak")
                pass
    else:
        print("Tidak ada gadget.")
    
# ----------------------------------------------------------------------------- F09 Kembalikan Gadget & FB02 Mengembalikan Gadget Secara Parsial ----------------------------------------------------------------------------- 
def balikin_gadget():
    
    #Cek dulu dia udah pernah minjem barang atau tidak
    for i in range (len(gadget_borrow_history_matrix)):
        if (active_user == gadget_borrow_history_matrix[i][1]):
            print("History peminjaman gadget oleh", nama_user)
            for i in range (len(gadget_borrow_history_matrix)):
                if (active_user == gadget_borrow_history_matrix[i][1]):
                    print(gadget_borrow_history_matrix[i][0:4])  
                    
            #Karena udah tau mminjem apa aja, nanti kita tanya mau balikkin yang mana        
            id = input("Masukkan ID gadget yang mau dikembalikan : ")
            
            #Kita cari indeks buat diubah jumlahnya
            indeks = 0              
            for i in range (len(gadget_matrix)):
                if (id == gadget_matrix[i][0]):
                    indeks = i
                    break
                
            #Kita cari indeks buat ngubah jumlah stok_user di gadget_borrow_history_matrix_history.csv    
            idx = 0          
            for i in range (len(gadget_borrow_history_matrix)):
                if (active_user == gadget_borrow_history_matrix[i][1] and id == gadget_borrow_history_matrix[i][2]):
                    idx = i
                    break
            
            if (indeks != 0 and idx != 0):
                #Ini harus diitung dulu user punya/udah minjem berapa jadi dia balikkinnya ga kebanyakan
                #Karena kalo udah minjem gaboleh minjem yang sama jadi diubah kayak gini
                stok_user = int(gadget_borrow_history_matrix[idx][5])

                print("Stok yang Anda miliki : ", stok_user)
                #Gabisa 0 juga karena kalo abis kembaliin 0 kan didelete
                # if (stok_user != 0): 
                berapa = int(input("Mau kembalikan berapa : "))
                    
                if (1 <= berapa <= stok_user):
                    gadget_matrix[indeks][3] = gadget_matrix[indeks][3] + berapa
                    print("Item", gadget_matrix[indeks][1], "sebanyak", berapa, "telah dikembalikan.")
                    global balikin_history
                    balikin_history = [int(gadget_return_history_matrix[-1][0])+1,gadget_borrow_history_matrix[idx][0],tanggal,berapa]
                    gadget_borrow_history_matrix[idx][5] = stok_user - berapa
                    if(gadget_borrow_history_matrix[idx][5] == 0):
                        gadget_borrow_history_matrix.remove(gadget_borrow_history_matrix[idx])
                    else:
                        pass
                    
                elif (berapa >= stok_user):
                    print("Anda tidak punya gadget sebanyak itu!")
                    
                else:
                    print("Harus lebih dari 0.")
                pass
            else:
                print("Anda tidak memiliki gadget ini.")
            break
    else:
        print("User tidak sedang meminjam gadget!")

# ----------------------------------------------------------------------------- F10 Minta Consumable ----------------------------------------------------------------------------- 
def minta_consumables():
    id = input("Masukkan ID consumable : ")
    indeks = 0
    #Kita cari indeks buat diubah jumlahnya
    for i in range (len(consumable_matrix)):
        if (id == consumable_matrix[i][0]):
            indeks = i
            break
    else:
        print("Tidak ada consumable")
        
    if(indeks != 0):                   
        print("Stok yang tersedia : ", consumable_matrix[indeks][3])  
        jumlah = int(input("Jumlah yang diminta : "))
        #Karena udah tau indeksnya, kita bisa ngambil dari stok gudang berapa yang si user mau                    
        if (1 <= jumlah <= consumable_matrix[indeks][3]):
            consumable_matrix[indeks][3] = consumable_matrix[indeks][3] - jumlah
            print("Item", consumable_matrix[indeks][1], "sebanyak", str(jumlah),"telah diambil." )
            #Buat masukin ke consumable_history.csv
            global consumable_sejarah
            consumable_sejarah = [int(consumable_history_matrix[-1][0])+1,active_user, id, tanggal, jumlah, jumlah]
        elif (jumlah <= 0):
            print("Jumlah harus lebih dari 0")
        else:
            print("Jumlah yang diminta terlalu banyak") 
    else:
        pass
    
# ----------------------------------------------------------------------------- F11 Riwayat Pinjam -----------------------------------------------------------------------------

def riwayatpinjam():   

     #sorted descending array gadget_borrow_history_matrix sesuai tanggal
    sortdesctgl=[[ 0 for a in range (2)] for b in range (len(gadget_borrow_history_matrix)-1)]
    for a in range (1, len(gadget_borrow_history_matrix)):
        sortdesctgl[a-1][0]=int(gadget_borrow_history_matrix[a][3][6]+gadget_borrow_history_matrix[a][3][7]+gadget_borrow_history_matrix[a][3][8]+gadget_borrow_history_matrix[a][3][9]+gadget_borrow_history_matrix[a][3][3]+gadget_borrow_history_matrix[a][3][4]+gadget_borrow_history_matrix[a][3][0]+gadget_borrow_history_matrix[a][3][1])
        sortdesctgl[a-1][1]=str(gadget_borrow_history_matrix[a][0]) #menyimpan id peminjaman
    
    sortdesctgl.sort(reverse=True) #list telah disort descending berdasarkan tanggal
    banyakdata=len(sortdesctgl)

    print("Menampilkan 5 Riwayat Peminjaman Gadget Terbaru\n")
        
    for a in range (banyakdata):

        for b in range (len(gadget_borrow_history_matrix)):

            if (str(gadget_borrow_history_matrix[b][0]))==str(sortdesctgl[a][1]): #mencocokkan id peminjaman
                print("ID Peminjaman     :", gadget_borrow_history_matrix[b][0])
                
                for c in range (len(user_matrix)): #mencocokkan nama pengambil
                    if (user_matrix[c][0])==(gadget_borrow_history_matrix[b][1]):
                        print("Nama Pengambil    :", user_matrix[c][2])

                for d in range (len(gadget_matrix)):
                    if (gadget_matrix[d][0])== (gadget_borrow_history_matrix[b][2]): #mencocokkan nama gadget
                        print("Nama Gadget       :", gadget_matrix[d][1])

                print("Tanggal Peminjaman:", gadget_borrow_history_matrix[b][3])
                print("Jumlah            :",  gadget_borrow_history_matrix[b][4], "\n")

        if (a%5==4):
            lanjut=input("Ingin menampilkan entry selanjutnya? (Y/N): ")
            if lanjut.lower()=="y":
                print()
                continue
            else:
                break

# ----------------------------------------------------------------------------- F12 Riwayat Kembali -----------------------------------------------------------------------------

def riwayatkembali():
   
     #sorted descending array gadget_return_history_matrix sesuai tanggal
    sortdesctgl=[[0 for a in range (2)] for b in range (len(gadget_return_history_matrix))]
    for a in range (1, len(gadget_return_history_matrix)):
        sortdesctgl[a-1][0]=int(gadget_return_history_matrix[a][2][6]+gadget_return_history_matrix[a][2][7]+gadget_return_history_matrix[a][2][8]+gadget_return_history_matrix[a][2][9]+gadget_return_history_matrix[a][2][3]+gadget_return_history_matrix[a][2][4]+gadget_return_history_matrix[a][2][0]+gadget_return_history_matrix[a][2][1])
        sortdesctgl[a-1][1]=str(gadget_return_history_matrix[a][0]) #menyimpan id peminjaman
    
    sortdesctgl.sort(reverse=True) #list telah disort descending berdasarkan tanggal
    banyakdata=len(sortdesctgl)

    print("Menampilkan 5 Riwayat Pengembalian Gadget Terbaru\n")
        
    for a in range (banyakdata):

        for b in range (len(gadget_return_history_matrix)):
            if (str(gadget_return_history_matrix[b][0]))==str(sortdesctgl[a][1]): #mencocokkan id pengembalian
                print("ID Pengembalian     :", gadget_return_history_matrix[b][0])

                for c in range (len(gadget_borrow_history_matrix)): #mencocokkan id peminjaman
                    if (gadget_borrow_history_matrix[c][0])==(gadget_return_history_matrix[b][1]):
                        for d in range (len(user_matrix)): #mencocokkan nama pengambil
                            if (user_matrix[d][0])==(gadget_borrow_history_matrix[c][1]):
                                print("Nama Pengambil      :", user_matrix[d][2])
                        
                        for e in range (len(gadget_matrix)):
                            if (gadget_matrix[e][0])== (gadget_borrow_history_matrix[c][2]): #mencocokkan nama gadget
                                print("Nama Gadget         :", gadget_matrix[e][1])
                        print("Tanggal Pengembalian:", gadget_return_history_matrix[b][2], "\n")
      
        if (a%5==4):
            lanjut=input("Ingin menampilkan entry selanjutnya? (Y/N): ")
            if lanjut.lower()=="y":
                print()
                continue
            else:
                break



# ----------------------------------------------------------------------------- F13 Riwayat Ambil -----------------------------------------------------------------------------

def riwayatambil():

     #sorted descending array consumable_history_matrix sesuai tanggal
    sortdesctgl=[[0 for a in range (2)] for b in range (len(consumable_history_matrix)-1)]
    for a in range (1, len(consumable_history_matrix)):
        sortdesctgl[a-1][0]=int(consumable_history_matrix[a][3][6]+consumable_history_matrix[a][3][7]+consumable_history_matrix[a][3][8]+consumable_history_matrix[a][3][9]+consumable_history_matrix[a][3][3]+consumable_history_matrix[a][3][4]+consumable_history_matrix[a][3][0]+consumable_history_matrix[a][3][1])
        sortdesctgl[a-1][1]=str(consumable_history_matrix[a][0]) #menyimpan id peminjaman

    sortdesctgl.sort(reverse=True) #list telah disort descending berdasarkan tanggal
    banyakdata=len(sortdesctgl)

    print("\nMenampilkan 5 Riwayat Pengambilan Consumable Terbaru\n")
        
    for a in range (banyakdata):
        for b in range (len(consumable_history_matrix)):
            if (str(consumable_history_matrix[b][0]))==str(sortdesctgl[a][1]): #mencocokkan id peminjaman
                print("ID Pengambilan     :", consumable_history_matrix[b][0])
                for c in range (len(user_matrix)): #mencocokkan nama peminjam
                    if (user_matrix[c][0])==(consumable_history_matrix[b][1]):
                        print("Nama Pengambil     :", user_matrix[c][2])
                for d in range (len(consumable_matrix)):
                    if (consumable_matrix[d][0])== (consumable_history_matrix[b][2]): #mencocokkan nama consumable
                        print("Nama Consumable    :", consumable_matrix[d][1])
                print("Tanggal Pengambilan:", consumable_history_matrix[b][3])
                print("Jumlah             :", consumable_history_matrix[b][4], "\n")
       
        if (a%5==4):
            lanjut=input("Ingin menampilkan entry selanjutnya? (Y/N): ")
            if lanjut.lower()=="y":
                print()
                continue
            else:
                break
# ----------------------------------------------------------------------------- F14 Loading data ----------------------------------------------------------------------------- 
def load_data():
    
    # Membaca argument pada commandline saat mengeksekusi file
    try:
        cwd = os.getcwd()
        os.chdir(sys.argv[1])

        # load .csv dari folder
        global user_matrix
        global consumable_matrix
        global consumable_history_matrix
        global gadget_matrix
        global gadget_borrow_history_matrix
        global gadget_return_history_matrix

        user_matrix = csv_to_matrix("user.csv")
        consumable_matrix = csv_to_matrix("consumable.csv")
        gadget_matrix = csv_to_matrix("gadget.csv")
        consumable_history_matrix = csv_to_matrix("consumable_history.csv")
        gadget_borrow_history_matrix = csv_to_matrix("gadget_borrow_history.csv")
        gadget_return_history_matrix = csv_to_matrix("gadget_return_history.csv")


        print("Semua data terload")

    except IndexError:
        print("Tidak ada nama Folder yang diberikan!")
        exit()
    except FileNotFoundError:
        print("Folder tidak ditemukan!")
        exit()
    os.chdir(cwd)


# ----------------------------------------------------------------------------- F15 Save Data ----------------------------------------------------------------------------- 
def save_data():
    folder = str(input("Masukkan nama folder penyimpanan: "))
    # cek jika sudah ada folder dengan nama sama
    if not os.path.exists(folder):
        os.makedirs(folder)

    # ganti working directory ke folder tujan
    os.chdir(folder)
    # Ubah matrix ke string
    user_matrix_string = data_matrix_to_string(user_matrix)
    consumable_matrix_string = data_matrix_to_string(consumable_matrix)
    consumable_history_matrix_string = data_matrix_to_string(consumable_history_matrix)
    gadget_matrix_string = data_matrix_to_string(gadget_matrix)
    gadget_borrow_history_matrix_string = data_matrix_to_string(gadget_borrow_history_matrix)
    gadget_return_history_matrix_string = data_matrix_to_string(gadget_return_history_matrix)
    # Tulis string ke file .csv
    write_data(user_matrix_string,"user.csv")
    write_data(consumable_matrix_string,"consumable.csv")
    write_data(consumable_history_matrix_string,"consumable_history.csv")
    write_data(gadget_matrix_string,"gadget.csv")
    write_data(gadget_borrow_history_matrix_string,"gadget_borrow_history.csv")
    write_data(gadget_return_history_matrix_string,"gadget_return_history.csv")

    print("Semua data tersimpan!")

# ----------------------------------------------------------------------------- F16 Help ----------------------------------------------------------------------------- 
def help():
    print("===================================================== HELP ==========================================================")
    print("| register            : Melakukan registrasi untuk user baru (for admin only)                                       |")
    print("| cari rarity         : Mencari gadget berdasarkan rarity gadget                                                    |")
    print("| cari tahun          : Mencari gadget berdasarkan tahun ditemukannya                                               |")
    print("| tambah item         : Menambah item gadget atau consumable ke dalam database Kantong Ajaib (for admin only)       |")
    print("| hapus item          : Menghapus item gadget atau consumable dari database Kantong Ajaib (for admin only)          |")
    print("| ubah jumlah         : Mengubah jumlah stok item gadget atau consumable di database Kantong Ajaib (for admin only) |")
    print("| pinjam gadget       : Meminjam gadget dari Kantong Ajaib (for user only)                                          |")
    print("| kembalikan gadget   : Mengembalikan gadget yang telah dipinjam (for user only)                                    |")
    print("| minta consumable    : Meminta consumable yang tersedia (for user only)                                            |")
    print("| gacha               : Meningkatkan rarity consumable (for user only)                                              |")
    print("| riwayat pinjam      : Melihat riwayat peminjaman gadget Kantong Ajaib (for admin only)                            |")
    print("| riwayat kembali     : Melihat riwayat pengembalian gadget Kantong Ajaib (for admin only)                          |")
    print("| riwayat ambil       : Melihat riwayat pengambilan consumable Kantong Ajaib (for admin only)                       |")
    print("| save                : Menyimpan perubahan yang telah dilakukan                                                    |")
    print("| help                : Untuk menampilkan bantuan sistem Kantong Ajaib                                              |")
    print("| exit                : Keluar sistem                                                                               |")   
    print("=====================================================================================================================")  
    print() 
# -----------------------------------------------------------------------------  FB01 Hashing  -----------------------------------------------------------------------------  
def my_encrypt(key, string):
    arr1 = []
    arr2 = []

    for i in string:
        elmt = ord(i)
        arr1.append(elmt)
        
    for j in range(len(string)):
        elmt = ord(key[j % len(key)]) 
        arr2.append(elmt)

    encryptedarray = [(arr1[i] + arr2[i]) % 127 for i in range(len(string))]
    encryptedstring = [chr(encryptedarray[i]) for i in range(len(encryptedarray))]

    return "".join(encryptedstring)
    
# ----------------------------------------------------------------------------- FB03 Meningkatkan rarity consumable ----------------------------------------------------------------------------- 
def inventory_consumable():
    count = 0
    #Buat nyari panjang consumable_user dulu
    for i in range (len(consumable_history_matrix)):
        for j in range(len(consumable_matrix)):
            if (active_user == consumable_history_matrix[i][1] and consumable_history_matrix[i][2] == consumable_matrix[j][0]):
                count += 1

    global consumable_user   
    consumable_user = [["*" for p in range (4)]for q in range (count)]
    k = 0
    for i in range (len(consumable_history_matrix)):
        for j in range(len(consumable_matrix)):
            if (active_user == consumable_history_matrix[i][1] and consumable_history_matrix[i][2] == consumable_matrix[j][0]):
                consumable_user[k][0] = k+1
                consumable_user[k][1] = consumable_matrix[j][1]
                consumable_user[k][2] = consumable_matrix[j][4]
                consumable_user[k][3] = consumable_history_matrix[i][5]
                k += 1
    for i in range (len(consumable_user)):
        consumable_user[i][3] = int(consumable_user[i][3])

def tanya_consumable():
    indeks = -1
    idx = -1
    valid = 0
    jumlah = 0
    global angka_gacha
    print("===================================== INVENTORY", nama_user, "========================================")
    for i in range (len(consumable_user)):
        print(consumable_user[i][0], end="")
        print(".", consumable_user[i][1],end="")
        print(", Rarity", consumable_user[i][2],end="")
        print(",", consumable_user[i][3])
    print("==============================================================================================")
    id_consumable = int(input("Pilih consumable yang mau digunakan: "))
    for i in range(len(consumable_user)):
        if (id_consumable == consumable_user[i][0]):
            indeks = i
            valid += 1
            banyak = int(input("Pilih jumlah yang mau digunakan: "))
            if(1 <= banyak <= consumable_user[indeks][3]):
                #Buat ganti history
                jumlah = consumable_user[indeks][3]
                consumable_user[indeks][3] = consumable_user[indeks][3] - banyak
                print(consumable_user[indeks][1], "(x", end="")
                print(banyak, end="") 
                print(") telah ditambahkan!")
                if (consumable_user[indeks][2] == "C"):
                    angka_gacha += (0.1*banyak)
                elif (consumable_user[indeks][2] == "B"):
                    angka_gacha += (1*banyak)
                elif (consumable_user[indeks][2] == "A"):
                    angka_gacha += (10*banyak)
                elif (consumable_user[indeks][2] == "S"):
                    angka_gacha += (100*banyak)
                break
            else:
                print("Jumlah tidak valid")
                break
    else:
        print("Tidak ada consumable")

    if(0.0001 <= angka_gacha <= 2):
        print("Kemungkinan mendapatkan rarity C 100 %")
    elif(2.1 <= angka_gacha <= 20):
        print("Kemungkinan mendapatkan rarity B",angka_gacha*10/2, "%")
    elif (20.1 <= angka_gacha <= 200):
        print("Kemungkinan mendapatkan rarity A",angka_gacha/2, "%")
    elif (200.1 <= angka_gacha <= 2000):
        print("Kemungkinan mendapatkan rarity S", angka_gacha/20, "%")
    elif (2000.1 <= angka_gacha <= 200000000):
        print("Kemungkinan mendapatkan rarity S 100 %")

    for i in range (len(consumable_matrix)):
        if(consumable_matrix[i][1] == consumable_user[indeks][1]):
            idx = i
            break

    if(valid != 0 and indeks != -1 and idx != -1):
        for i in range (len(consumable_history_matrix)):
            if(consumable_history_matrix[i][2] == consumable_matrix[idx][0] and str(jumlah) == consumable_history_matrix[i][5]):
                consumable_history_matrix[i][5] = str(consumable_user[indeks][3])
                if(consumable_user[indeks][3] == 0):
                    consumable_user.remove(consumable_user[indeks])
                    consumable_history_matrix.remove(consumable_history_matrix[i])
                    break

    return angka_gacha
    return consumable_user
    return consumable_history_matrix

def angka_random():

    base = 123456789
    a = 135809
    c = 1313
    m = (2 ** 16)
    base = (a * base + c) % m
    time.localtime()
    second = time.localtime().tm_sec
    global acak
    if (second != 0 and second > 9):
        acak = round(((base/m) *60/second), 5)
    elif(3 >= second >= 0):
        acak = round(((base/m) *60/30), 5)
    elif(8 >= second >= 4):
        acak = round((base/m) *60/45,5)
    else:
        acak = round((base/m) *60/55,5)
    #Angka random di interval [0.85..5]
    return acak
    
def penentu_consumable():

    angka_random()
    angka = angka_gacha*acak
    consumable_hasil_gacha = []
    print("...Rolling...")
    if (0.001 <= angka <= 10):
        for i in range (len(consumable_matrix)):
            if (consumable_matrix[i][4] == "C"):
                print("Selamat, Anda mendapatkan", consumable_matrix[i][1], "(Rarity", consumable_matrix[i][4], end="")
                print(")!")
                consumable_hasil_gacha = [int(consumable_history_matrix[-1][0])+1+1, active_user, consumable_matrix[i][0], tanggal, 1, 1] 
                break
        consumable_history_matrix.append(consumable_hasil_gacha)
    elif (11 <= angka <= 100):
        for i in range (len(consumable_matrix)):
            if (consumable_matrix[i][4] == "B"):
                print("Selamat, Anda mendapatkan", consumable_matrix[i][1], "(Rarity", consumable_matrix[i][4], end="")
                print(")!")
                consumable_hasil_gacha = [int(consumable_history_matrix[-1][0])+1, active_user, consumable_matrix[i][0], tanggal, 1, 1] 
                break
        consumable_history_matrix.append(consumable_hasil_gacha)
    elif (101 <= angka <= 1000):
        for i in range (len(consumable_matrix)):
            if (consumable_matrix[i][4] == "A"):
                print("Selamat, Anda mendapatkan", consumable_matrix[i][1], "(Rarity", consumable_matrix[i][4], end="")
                print(")!")
                consumable_hasil_gacha = [int(consumable_history_matrix[-1][0])+1+1, active_user, consumable_matrix[i][0], tanggal, 1, 1] 
                break
        consumable_history_matrix.append(consumable_hasil_gacha)
    elif (1001 <= angka <= 10000000000):
        for i in range (len(consumable_matrix)):
            if (consumable_matrix[i][4] == "S"):
                print("Selamat, Anda mendapatkan", consumable_matrix[i][1], "(Rarity", consumable_matrix[i][4], end="")
                print(")!")
                consumable_hasil_gacha = [int(consumable_history_matrix[-1][0])+1+1, active_user, consumable_matrix[i][0], tanggal, 1, 1] 
                break
        consumable_history_matrix.append(consumable_hasil_gacha)

def gacha():
    inventory_consumable()
    global angka_gacha
    angka_gacha = 0
    tanya = True
    while (tanya and len(consumable_user) != 0):
        nanya = input("Tambahkan consumable? (Y/N) : ")
        if (nanya == "Y" or nanya == "y"):
            tanya_consumable()
        elif (nanya == "N" or nanya == "n"):
            tanya = False
        else:
            print("Input tidak valid")
    penentu_consumable()
        
# ----------------------------------------------------------------------------- #### PROGRAM UTAMA #### ----------------------------------------------------------------------------- 
# F14
# Load data akan berjalan secara otomatis
load_data()

# Data telah terload
print()
print()
print("                       ---------------------------------------------------------------------")
print("                       | Selamat datang di Inventarisasi Kantong Ajaib milik Doremonangis! |")
print("                       ---------------------------------------------------------------------")

# Pemaparan bantuan command, help dapat dipanggil kembali jika user butuh
help()
run = True

# Program berjalan
while run:

    # F02
    state = login()

    if state == "User" or state == "Admin": 
        loggedOn = True

        while loggedOn: 
            print()

            action = str(input("Mau ngapain?? "))

            # F15
            if action == "save":

                save_data()
                loggedOn = True
            
            # F17
            elif action == "exit":

                quitSave = str(input("Mau save dulu tidak? (Y/N) "))
                if quitSave == "y" or quitSave == "Y":
                    save_data()
                elif quitSave == "n" or quitSave == "N": 
                    pass
                print("quitting...")
                print()
                print("                       ---------------------------------------------------------------------")
                print("                       |                            Sampai jumpa!                          |")
                print("                       ---------------------------------------------------------------------")
                loggedOn = False
                run = False

            # F01
            elif action == "register":

                if state == "Admin":
                    register()
                    loggedOn = True
                else: 
                    print("Hanya admin yang dapat menggunakan fitur ini!")
                    loggedOn = True

            # F03
            elif action == "cari rarity":
                cariGadgetRarity()
                loggedOn = True

            # F04
            elif action == "cari tahun":
                cariGadgetTahun()
                loggedOn = True

            # F05
            elif action == "tambah item":
                if state == "Admin":
                    tambahitem()
                    loggedOn = True
                else:
                    print("Hanya admin yang dapat menggunakan fitur ini!")
                    loggedOn = True

            # F06
            elif action == "hapus item":
                if state == "Admin":
                    hapusitem()
                    loggedOn = True
                else:
                    print("Hanya admin yang dapat menggunakan fitur ini!")
                    loggedOn = True

            # F07
            elif action == "ubah jumlah":
                if state == "Admin":
                    ubahjumlah()
                    loggedOn = True
                else:
                    print("Hanya admin yang dapat menggunakan fitur ini!")
                    loggedOn = True

            # F08
            elif action == "pinjam gadget":
                pinjam_history = []
                if state == "User":
                    pinjam_gadget()
                    if (pinjam_history != []):
                        gadget_borrow_history_matrix.append(pinjam_history)
                    gadget_matrix_string = data_matrix_to_string(gadget_matrix)
                    gadget_borrow_history_matrix_string = data_matrix_to_string(gadget_borrow_history_matrix)
                    loggedOn = True
                else:
                    print("Hanya user yang dapat menggunakan fitur ini!")
                    loggedOn = True

            # F09
            elif action == "kembalikan gadget":
                if state == "User":
                    balikin_history = []
                    balikin_gadget()
                    if (balikin_history != []):
                        gadget_return_history_matrix.append(balikin_history)
                    gadget_matrix_string = data_matrix_to_string(gadget_matrix)
                    gadget_return_history_matrix_string = data_matrix_to_string(gadget_return_history_matrix)
                    gadget_borrow_history_matrix_string = data_matrix_to_string(gadget_borrow_history_matrix)
                    loggedOn = True
                else:
                    print("Hanya user yang dapat menggunakan fitur ini!")
                    loggedOn = True

            # F10
            elif action == "minta consumable":
                consumable_sejarah = []
                if state == "User":
                    minta_consumables()
                    if (consumable_sejarah != []): 
                        consumable_history_matrix.append(consumable_sejarah)
                    consumable_matrix_string = data_matrix_to_string(consumable_matrix)
                    consumable_history_matrix_string = data_matrix_to_string(consumable_history_matrix)
                    loggedOn = True
                else:
                    print("Hanya user yang dapat menggunakan fitur ini!")
                    loggedOn = True

            # F11
            elif action == "riwayat pinjam":
                if state == "Admin":
                    riwayatpinjam()
                    loggedOn = True
                else:
                    print("Hanya admin yang dapat menggunakan fitur ini!")
                    loggedOn = True

            # F12
            elif action == "riwayat kembali":
                if state == "Admin":
                    riwayatkembali()
                    loggedOn = True
                else:
                    print("Hanya admin yang dapat menggunakan fitur ini!")
                    loggedOn = True

            # F13
            elif action == "riwayat ambil":
                if state == "Admin":
                    riwayatambil()
                    loggedOn = True
                else:
                    print("Hanya admin yang dapat menggunakan fitur ini!")
                    loggedOn = True

            # F16
            elif action == "help":
                help()
                loggedOn = True
            
            # FB03
            elif action == "gacha":
                if state == "User":
                    gacha()
                else:
                    print("Hanya user yang dapat menggunakan fitur ini!")
                    loggedOn = True
                    
            else:
                print("Invalid command, ketik 'help' untuk melihat semua list command.")
                loggedOn = True

    elif state == "Not logged in":
        run = True

#python TugasBesarIF1210.py tempatSimpan  
