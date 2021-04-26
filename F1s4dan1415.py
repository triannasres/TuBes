import os
import sys
import math
import time 
import argparse
import datetime


##### FUNGSI PEMBANTU ######

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
                arr_copy[i] = int(arr_copy[i])
        return arr_copy
    elif x == "consumable.csv":
        for i in range(5):
            if i == 0:
                arr_copy[i] = str(arr_copy[i])
            elif i == 3:
                arr_copy[i] = int(arr_copy[i])
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
            if i == 4:
                arr_copy[i] = int(arr_copy[i])
        return arr_copy
    elif x == "gadget_borrow_history.csv":
        for i in range(5):
            if i == 4:
                arr_copy[i] = int(arr_copy[i])
        return arr_copy
    elif x == "gadget_return_history.csv":
        for i in range(4):
            if i == 1:
                arr_copy[i] = int(arr_copy[i])
        return arr_copy


# fungsi penyatu
def csv_to_matrix(name):
    f = open(name, "r")
    f_lines = f.readlines()
    print(f_lines)
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
        fNew = open(name, "w")
        fNew.write(string)


# Enkripsi 

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



##### FUNGSI SPESIFIKASI ######

# F01 Register

def register():
    noID = len(user_matrix)
    print(noID)
    nama = str(input("Masukan nama: "))
    username = str(input("Masukan username: "))
    password = my_encrypt(username, str(input("Masukan password: ")))
    alamat = str(input("Masukan alamat: "))

    array = [noID,username,nama.title(),alamat,password,"user"]

    user_matrix.append(array)

    print("User", username, "telah berhasil register ke dalam Kantong Ajaib.")

# F02 Login

def login():

    username = str(input("Masukan username: "))
    
    for i in range(len(user_matrix)):
        if user_matrix[i][1] == username:
            print(i)
            print(user_matrix[i][4])
            password = str(input("Masukan password: "))
            print(my_encrypt(username, password))
            if user_matrix[i][4] == my_encrypt(username, password):
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

        
# F03 Cari Gadget Berdasarkan Rarity

def cariGadgetRarity():
    rarity = str(input("Masukkan rarity: "))

    rarityList = []

    for i in range(1,len(gadget_matrix)):
        rarityList.append(gadget_matrix[i][4])
    print(rarityList)

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

# F04 Cari Gadget Berdasarkan tahun ditemukan

def cariGadgetTahun():
    tahun = int(input("Masukkan tahun: "))
    kategori = str(input("Masukkan kategori: "))

    if kategori == ">" or kategori == "<" or kategori == "<=" or kategori == ">=" or kategori == "=":
        tahunList = []

        for i in range(1, len(gadget_matrix)):
            tahunList.append(gadget_matrix[i][5])
        print(tahunList)

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

    





# F14 Loading data
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

        print(user_matrix)


        print("Semua data terload")
        os.chdir(cwd)
        return True
    except IndexError:
        print("Tidak ada nama Folder yang diberikan!")
        return False

    

# F15 Save Data
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



# PROGRAM UTAMA
if load_data():
    run = True

    while run:

        state = login()

        if state == "User" or state == "Admin": 

            loggedOn = True

            while loggedOn: 

                action = str(input("mau ngapain?? "))
                if action == "save":

                    save_data()
                    loggedOn = True
                elif action == "exit":

                    quitSave = str(input("Mau save dulu tidak? (y/n) "))
                    if quitSave == "y" or quitSave == "Y":
                        save_data()
                    elif quitSave == "n" or quitSave == "N": 
                        pass
                    print("quitting...")
                    loggedOn = False
                    run = False

                elif action == "register":

                    if state == "Admin":
                        register()
                        loggedOn = True
                    else: 
                        print("Kamu tidak bisa meregister sebagai user!")
                        loggedOn = True

                elif action == "carirarity":
                    cariGadgetRarity()
                    loggedOn = True

                elif action == "caritahun":
                    cariGadgetTahun()
                    loggedOn = True

        elif state == "Not logged in":
            run = True