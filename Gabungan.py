#INI BARU F08,F09,F10,F14,15

#Meminjam gadget
import os
import sys
import math
import time 
import argparse
import datetime

from functionsTubes import *

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
    if x == "consumable.csv":
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
        for i in range(6):
            if i == 4:
                arr_copy[i] = int(arr_copy[i])
            if i == 5:
                arr_copy[i] = int(arr_copy[i])
        return arr_copy
    elif x == "gadget_return_history.csv":
        for i in range(5):
            if i == 4:
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

#fungsi pinjam gadget
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
            jumlah = int(input("Jumlah peminjaman : "))
            #Karena udah tau indeksnya, kita bisa ngambil dari stok gudang berapa yang si user mau                    
            if (jumlah <= gadget_matrix[indeks][3]):
                gadget_matrix[indeks][3] = gadget_matrix[indeks][3] - jumlah
                print("Item", gadget_matrix[indeks][1], "sebanyak", str(jumlah),"telah dipinjam." )
            else:
                print("Jumlah peminjaman terlalu banyak")
            stok_user = jumlah
            #Data buat masuk history
            global pinjam_history
            pinjam_history = [len(gadget_borrow_history_matrix),active_user, id, tanggal, jumlah, stok_user]
    else:
        print("Tidak ada gadget ")
    
    
#fungsi balikkin gadget
def balikin_gadget():
    
    #Cek dulu dia udah pernah minjem barang atau tidak
    for i in range (len(gadget_borrow_history_matrix)):
        if (active_user in gadget_borrow_history_matrix[i][1]):
            print("History peminjaman gadget oleh", active_user)
            for i in range (len(gadget_borrow_history_matrix)):
                if (active_user == gadget_borrow_history_matrix[i][1]):
                    print(gadget_borrow_history_matrix[i][0:4])  
                    
            #Karena udah tau mminjem apa aja, nanti kita tanya mau balikkin yang mana        
            id = input("Masukkan ID gadget yang mau dibalikkin : ")
            
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

                print("Stok yang anda miliki : ",stok_user)
                #Bonus 2 yay
                if (stok_user != 0): 
                    berapa = int(input("Mau balikkin berapa : "))
                    
                    if (1 <= berapa <= stok_user):
                        gadget_matrix[indeks][3] = gadget_matrix[indeks][3] + berapa
                        print("Item", gadget_matrix[indeks][1], "sebanyak", berapa, "telah dikembalikan.")
                        global balikin_history
                        balikin_history = [len(gadget_return_history_matrix),active_user, id, tanggal, berapa]
                        gadget_borrow_history_matrix[idx][5] = stok_user - berapa
                        
                    elif (berapa >= stok_user):
                        print("Anda tidak punya gadget sebanyak itu")
                        
                    else:
                        print("Harus lebih dari 0")
                    break
                else:
                    print("Anda sudah tidak punya gadget ini")
                break
            else:
                print("Anda tidak memiliki ini")
    else:
        print("User tidak pernah meminjam gadget")

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
        if (jumlah <= consumable_matrix[indeks][3]):
            consumable_matrix[indeks][3] = consumable_matrix[indeks][3] - jumlah
            print("Item", consumable_matrix[indeks][1], "sebanyak", str(jumlah),"telah diambil." )
            #Buat masukin ke consumable_history.csv
            global consumable_sejarah
            consumable_sejarah = [len(consumable_history_matrix),active_user, id, tanggal, jumlah]
        else:
            print("Jumlah yang diminta terlalu banyak") 
    else:
        pass

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
        global active_user
        global tanggal

        # Bikin csv jadi matrix 
        user_matrix = csv_to_matrix("user.csv")
        consumable_matrix = csv_to_matrix("consumable.csv")
        gadget_matrix = csv_to_matrix("gadget.csv")
        consumable_history_matrix = csv_to_matrix("consumable_history.csv")
        gadget_borrow_history_matrix = csv_to_matrix("gadget_borrow_history.csv")
        gadget_return_history_matrix = csv_to_matrix("gadget_return_history.csv")

        #Biar pas save gak error kalo misalnya belom pernah ngelakuin salah satu hal (pinjam, balikkin, minta)
        #Kalo gaada gini nanti string ini ga kedefine belom kedefine
        user_matrix_string = data_matrix_to_string(user_matrix)
        consumable_matrix_string = data_matrix_to_string(consumable_matrix)
        consumable_history_matrix_string = data_matrix_to_string(consumable_history_matrix)
        gadget_matrix_string = data_matrix_to_string(gadget_matrix)
        gadget_borrow_history_matrix_string = data_matrix_to_string(gadget_borrow_history_matrix)
        gadget_return_history_matrix_string = data_matrix_to_string(gadget_return_history_matrix)

        waktu = datetime.date.today()
        tanggal = waktu.strftime("%d/%m/%Y")
        #Diganti ya nanti 
        active_user = "A006"

        print("Semua data terload")
    except IndexError:
        print("Tidak ada nama Folder yang diberikan!")

    os.chdir(cwd)


def save_data(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    os.chdir(folder)
    user_matrix_string = data_matrix_to_string(user_matrix)
    consumable_matrix_string = data_matrix_to_string(consumable_matrix)
    consumable_history_matrix_string = data_matrix_to_string(consumable_history_matrix)
    gadget_matrix_string = data_matrix_to_string(gadget_matrix)
    gadget_borrow_history_matrix_string = data_matrix_to_string(gadget_borrow_history_matrix)
    gadget_return_history_matrix_string = data_matrix_to_string(gadget_return_history_matrix)

    write_data(user_matrix_string,"user.csv")
    write_data(consumable_matrix_string,"consumable.csv")
    write_data(consumable_history_matrix_string,"consumable_history.csv")
    write_data(gadget_matrix_string,"gadget.csv")
    write_data(gadget_borrow_history_matrix_string,"gadget_borrow_history.csv")
    write_data(gadget_return_history_matrix_string,"gadget_return_history.csv")

    print("Semua data tersimpan!")

#buat terminal
run = True

while run: 
    load_data()
    action = str(input("mau ngapain?? "))

    if action == "pinjam":
        pinjam_history = []
        pinjam_gadget()
        if (pinjam_history != []):
            gadget_borrow_history_matrix.append(pinjam_history)
        gadget_matrix_string = data_matrix_to_string(gadget_matrix)
        gadget_borrow_history_matrix_string = data_matrix_to_string(gadget_borrow_history_matrix)
        # write_data(gadget,"gadget.csv")
        # write_data(gadget_borrow_history_matrix,"gadget_borrow_history_matrix_history.csv")
        # run = False
        
    elif action == "balikkin":
        balikin_history = []
        balikin_gadget()
        if (balikin_history != []):
            gadget_return_history_matrix.append(balikin_history)
        gadget_matrix_string = data_matrix_to_string(gadget_matrix)
        gadget_return_history_matrix_string = data_matrix_to_string(gadget_return_history_matrix)
        gadget_borrow_history_matrix_string = data_matrix_to_string(gadget_borrow_history_matrix)
        # write_data(gadget,"gadget.csv")
        # write_data(gadget_return,"gadget_return_history.csv")
        # write_data(gadget_borrow,"gadget_borrow_history.csv")
        # run = False
        
    elif action == "minta":
        consumable_sejarah = []
        minta_consumables()
        if (consumable_sejarah != []): 
            consumable_history_matrix.append(consumable_sejarah)
        consumable_matrix_string = data_matrix_to_string(consumable_matrix)
        consumable_history_matrix_string = data_matrix_to_string(consumable_history_matrix)
        # write_data(consumable,"consumable.csv")
        # write_data(consumable_history,"consumable_history.csv")
        # run = False
        
    elif action == "save":
        tempat = str(input("Masukkan nama folder penyimpanan: "))
        save_data(tempat)
        run = False

    elif action == "exit":
        run = False
