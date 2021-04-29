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
                arr_copy[i] = int(arr_copy[i])
            elif i == 1:
                arr_copy[i] = str(arr_copy[i])
            elif i == 2:
                arr_copy[i] = str(arr_copy[i])
            elif i == 4:
                arr_copy[i] = int(arr_copy[i])
        return arr_copy
    elif x == "gadget_borrow_history.csv":
        for i in range(5):
            if i == 0:
                arr_copy[i] = int(arr_copy[i])
            elif i == 1:
                arr_copy[i] = str(arr_copy[i])
            elif i == 2:
                arr_copy[i] = str(arr_copy[i])
            elif i == 4:
                arr_copy[i] = int(arr_copy[i])
        return arr_copy
    elif x == "gadget_return_history.csv":
        for i in range(3):
            if i == 0:
                arr_copy[i] = int(arr_copy[i])
            elif i == 1:
                arr_copy[i] = int(arr_copy[i])
        return arr_copy


# fungsi penyatu
def csv_to_matrix(name):
    f = open(name, "r")
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
        fNew = open(name, "w")
        fNew.write(string)

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



# F11 riwayatpinjam
# fungsi untuk menampilkan riwayat peminjaman gadget
def riwayatpinjam():   

    #sort tanggal
    sortedtanggal=[[ 0 for i in range (2)] for j in range (len(gadget_borrow_history_matrix)-1)]
    for i in range (1, len(gadget_borrow_history_matrix)-1):
        sortedtanggal[i][0]=int(gadget_borrow_history_matrix[i][3][6]+gadget_borrow_history_matrix[i][3][7]+gadget_borrow_history_matrix[i][3][8]+gadget_borrow_history_matrix[i][3][9]+gadget_borrow_history_matrix[i][3][3]+gadget_borrow_history_matrix[i][3][4]+gadget_borrow_history_matrix[i][3][0]+gadget_borrow_history_matrix[i][3][1])
        sortedtanggal[i][1]=str(gadget_borrow_history_matrix[i][0]) #menyimpan id peminjaman
    sortedtanggal.sort(reverse=True) #list telah disort descending berdasarkan tanggal
    banyakdata=len(sortedtanggal)
    print("Menampilkan 5 Riwayat Peminjaman Gadget Terbaru\n")
        
    for i in range (banyakdata):
        for j in range (len(gadget_borrow_history_matrix)):
            if (gadget_borrow_history_matrix[j][0])==str(sortedtanggal[i][1]): #mencocokkan id peminjaman
                print("ID Peminjaman    :", gadget_borrow_history_matrix[j][0])
                for k in range (len(user_matrix)): #mencocokkan nama pengambil
                    if (user_matrix[k][0])==(gadget_borrow_history_matrix[j][1]):
                        print("Nama Pengambil    :", user_matrix[k][2])
                for l in range (len(gadget_matrix)):
                    if (gadget_matrix[l][0])== (gadget_borrow_history_matrix[j][2]): #mencocokkan nama gadget
                        print("Nama Gadget    :", gadget_matrix[l][1])
                print("Tanggal Peminjaman:", gadget_borrow_history_matrix[j][3])
                print("Jumlah            :",  gadget_borrow_history_matrix[j][4], "\n")
        print(riwayatpinjam)

        if (i%5==4):
            lanjut=input("Ingin menampilkan entry selanjutnya? (Y/N): ")
            if lanjut.lower()=="y":
                print()
                continue
            else:
                break

# F12 riwayatkembali
# fungsi untuk menampilkan riwayat pengembalian gadget
def riwayatkembali():
    phrase1="Pengembalian"
    phrase2="Pengambil"
    phrase3="Gadget"

   
    #sort tanggal
    sortedtanggal=[[0 for i in range (2)] for j in range (len(gadget_return_history_matrix)-1)]
    for i in range (1, len(gadget_return_history_matrix)-1):
        sortedtanggal[i][0]=int(gadget_return_history_matrix[i][2][6]+gadget_return_history_matrix[i][2][7]+gadget_return_history_matrix[i][2][8]+gadget_return_history_matrix[i][2][9]+gadget_return_history_matrix[i][2][3]+gadget_return_history_matrix[i][2][4]+gadget_return_history_matrix[i][2][0]+gadget_return_history_matrix[i][2][1])
        sortedtanggal[i][1]=str()(gadget_return_history_matrix[i][0]) #menyimpan id peminjaman
    sortedtanggal.sort(reverse=True) #list telah disort descending berdasarkan tanggal
    banyakdata=len(sortedtanggal)
    print("\nMenampilkan 5 Riwayat Pengembalian Gadget Terbaru\n")
        
    for i in range (banyakdata):
        for j in range (len(gadget_return_history_matrix)):
            if (gadget_return_history_matrix[j][0])==str(sortedtanggal[i][1]): #mencocokkan id pengembalian
                print(f"ID {phrase1}     : {gadget_return_history_matrix[j][0]}")
                for k in range (len(gadget_borrow_history_matrix)): #mencocokkan id peminjaman
                    if (gadget_borrow_history_matrix[k][0])==(gadget_return_history_matrix[j][1]):
                        for m in range (len(user_matrix)): #mencocokkan nama pengambil
                            if (user_matrix[m][0])==(gadget_borrow_history_matrix[k][1]):
                                print("Nama Pengambil     :", user_matrix[m][2])
                        
                        for l in range (len(gadget_matrix)):
                            if (gadget_matrix[l][0])== (gadget_borrow_history_matrix[k][2]): #mencocokkan nama gadget
                                print("Nama Gadget   :", gadget_matrix[l][1])
                        print(f"Tanggal Pengembalian:" gadget_return_history_matrix[j][2], "\n")
        print()
        if (i%5==4):
            lanjut=input("Ingin menampilkan entry selanjutnya? (Y/N): ")
            if lanjut.lower()=="y":
                print()
                continue
            else:
                break



# F13 riwayat pengambilan consumable
# fungsi untuk menampilkan riwayat pengambilan consumable
def riwayatambil():
    phrase1="Pengambilan"
    phrase2="Pengambil"
    phrase3="Consumable"

    #sort tanggal
    sortedtanggal=[[0 for i in range (2)] for j in range (len(consumable_history_matrix)-1)]
    for i in range (1, len(consumable_history_matrix)-1):
        sortedtanggal[i][0]=int(consumable_history_matrix[i][3][6]+consumable_history_matrix[i][3][7]+consumable_history_matrix[i][3][8]+consumable_history_matrix[i][3][9]+consumable_history_matrix[i][3][3]+consumable_history_matrix[i][3][4]+consumable_history_matrix[i][3][0]+consumable_history_matrix[i][3][1])
        sortedtanggal[i][1]=str(consumable_history_matrix[i][0]) #menyimpan id peminjaman
    sortedtanggal.sort(reverse=True) #list telah disort descending berdasarkan tanggal
    banyakdata=len(sortedtanggal)
    print(f"Menampilkan 5 riwayat {phrase1} terbaru\n")
        
    for i in range (banyakdata):
        for j in range (len(consumable_history_matrix)):
            if (consumable_history_matrix[j][0])==str(sortedtanggal[i][1]): #mencocokkan id peminjaman
                print(f"ID {phrase1}     : {consumable_history_matrix[j][0]}")
                for k in range (len(user_matrix)): #mencocokkan nama peminjam
                    if (user_matrix[k][0])==(consumable_history_matrix[j][1]):
                        print(f"Nama {phrase2}     : {user_matrix[k][2]}")
                for l in range (len(consumable_matrix)):
                    if (consumable_matrix[l][0])== (consumable_history_matrix[j][2]): #mencocokkan nama consumable
                        print(f"Nama {phrase3}    : {consumable_matrix[l][1]}")
                print(f"Tanggal {phrase1}: {consumable_history_matrix[j][3]}")
                print(f"Jumlah             : {consumable_history_matrix[j][4]}")
        print()
        if (i%5==4):
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
    print("| pinjam gadget       : Meminjam gadget dari Kantong Ajaib                                                          |")
    print("| kembalikan gadget   : Mengembalikan gadget yang telah dipinjam                                                    |")
    print("| minta consumable    : Meminta consumable yang tersedia                                                            |")
    print("| riwayat pinjam      : Melihat riwayat peminjaman gadget Kantong Ajaib (for admin only)                            |")
    print("| riwayat kembali     : Melihat riwayat pengembalian gadget Kantong Ajaib (for admin only)                          |")
    print("| riwayat ambil       : Melihat riwayat pengambilan consumable Kantong Ajaib (for admin only)                       |")
    print("| save                : Menyimpan perubahan yang telah dilakukan                                                    |")
    print("| help                : Untuk menampilkan bantuan sistem Kantong Ajaib                                              |")
    print("| exit                : Keluar sistem                                                                               |")   
    print("=====================================================================================================================")  
    print() 


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
                    print("Kamu tidak bisa meregister sebagai user!")
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
                pinjam_gadget()
                if (pinjam_history != []):
                    gadget_borrow_history_matrix.append(pinjam_history)
                gadget_matrix_string = data_matrix_to_string(gadget_matrix)
                gadget_borrow_history_matrix_string = data_matrix_to_string(gadget_borrow_history_matrix)
                loggedOn = True

            # F09
            elif action == "kembalikan gadget":
                balikin_history = []
                balikin_gadget()
                if (balikin_history != []):
                    gadget_return_history_matrix.append(balikin_history)
                gadget_matrix_string = data_matrix_to_string(gadget_matrix)
                gadget_return_history_matrix_string = data_matrix_to_string(gadget_return_history_matrix)
                gadget_borrow_history_matrix_string = data_matrix_to_string(gadget_borrow_history_matrix)
                loggedOn = True

            # F10
            elif action == "minta consumable":
                consumable_sejarah = []
                minta_consumables()
                if (consumable_sejarah != []): 
                    consumable_history_matrix.append(consumable_sejarah)
                consumable_matrix_string = data_matrix_to_string(consumable_matrix)
                consumable_history_matrix_string = data_matrix_to_string(consumable_history_matrix)
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

    elif state == "Not logged in":
        run = True