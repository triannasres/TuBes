#Meminjam gadget
import os
import sys
import math
import time 
import argparse
import datetime

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

# Bikin gadget.csv sama gadget_borrow_history.csv jadi matrix 
gadget_list = csv_to_matrix("gadget.csv")
# print(gadget_list)
gadget_borrow = csv_to_matrix("gadget_borrow_history.csv")
# print(gadget_borrow)
gadget_return = csv_to_matrix("gadget_return_history.csv")
# print(gadget_return)
consumable_list = csv_to_matrix("consumable.csv")
# print(consumable_list)
consumable_history = csv_to_matrix("consumable_history.csv")
# print(consumable_history)
waktu = datetime.date.today()
tanggal = waktu.strftime("%d/%m/%Y")
#Diganti ya nanti 
active_user = "A001"

#fungsi pinjam gadget
def pinjam_gadget():
   
    id = input("Masukkan ID item : ")
    indeks = 0
    #Kita cari indeks buat diubah jumlahnya
    for i in range (len(gadget_list)):
        if (id == gadget_list[i][0]):
            indeks = i
            break
    else:
        print("Tidak ada gadget ")
        
    if(indeks != 0):     
        print("Stok yang tersedia : ", gadget_list[indeks][3])              
        jumlah = int(input("Jumlah peminjaman : "))
        #Karena udah tau indeksnya, kita bisa ngambil dari stok gudang berapa yang si user mau                    
        if (jumlah <= gadget_list[indeks][3]):
            gadget_list[indeks][3] = gadget_list[indeks][3] - jumlah
            print("Item", gadget_list[indeks][1], "sebanyak", str(jumlah),"telah dipinjam." )
        else:
            print("Jumlah peminjaman terlalu banyak")
        #Data buat masuk history
        global pinjam_history
        pinjam_history = [len(gadget_borrow),active_user, id, tanggal, jumlah]
    
    else:
        pass
    
#fungsi balikkin gadget
def balikin_gadget():
    
    if (active_user in gadget_borrow[0:len(gadget_borrow)][1]):
        print("History peminjaman gadget oleh", active_user)
        for i in range (len(gadget_borrow)):
            if (active_user == gadget_borrow[i][1]):
                print(gadget_borrow[i])  
                
        #Karena udah tau mminjem apa aja, nanti kita tanya mau balikkin yang mana        
        id = input("Masukkan ID gadget yang mau dibalikkin : ")
        
        #Ini harus diitung dulu user punya/udah minjem berapa jadi dia balikkinnya ga kebanyakan 
        stok_user = 0
        for i in range (len(gadget_borrow)):
            if (gadget_borrow[i][2] == id and active_user == gadget_borrow[i][1]):
                stok_user += gadget_borrow[i][4]

        print("Stok yang anda miliki : ",stok_user)
        
        indeks = 0              
        for i in range (len(gadget_list)):
            if (id == gadget_list[i][0]):
                indeks = i
                break
            
        if (id == gadget_borrow[indeks][2]): 
            berapa = int(input("Mau balikkin berapa : "))
            
            if(berapa <= stok_user):
                gadget_list[indeks][3] = gadget_list[indeks][3] + berapa
                print("Item", gadget_list[indeks][1], "sebanyak", berapa, "telah dikembalikan.")
                global balikin_history
                balikin_history = [len(gadget_return),active_user, id, tanggal, berapa]
            else:
                print("Ente tidak punya gadget sebanyak itu")
        else:
            print("Anda tidak memiliki gadget ini")
    else:
        print("User tidak pernah meminjam gadget")

def minta_consumables():
    
    id = input("Masukkan ID consumable : ")
    indeks = 0
    #Kita cari indeks buat diubah jumlahnya
    for i in range (len(consumable_list)):
        if (id == consumable_list[i][0]):
            indeks = i
            break
    else:
        print("Tidak ada consumable")
        
    if(indeks != 0):                   
        print("Stok yang tersedia : ", consumable_list[indeks][3])  
        jumlah = int(input("Jumlah yang diminta : "))
        #Karena udah tau indeksnya, kita bisa ngambil dari stok gudang berapa yang si user mau                    
        if (jumlah <= consumable_list[indeks][3]):
            consumable_list[indeks][3] = consumable_list[indeks][3] - jumlah
            print("Item", consumable_list[indeks][1], "sebanyak", str(jumlah),"telah dipinjam." )
            #Buat masukin ke consumable_history.csv
            global consumable_sejarah
            consumable_sejarah = [len(consumable_history),active_user, id, tanggal, jumlah]
        else:
            print("Jumlah yang diminta terlalu banyak") 
    else:
        pass
       
#buat terminal
run = True

while run: 

    action = str(input("mau ngapain?? "))

    if action == "pinjam gadget":
        pinjam_history = []
        pinjam_gadget()
        new_gadget = data_matrix_to_string(gadget_list)
        if (pinjam_history != []):
            gadget_borrow.append(pinjam_history)
        new_gadget_borrow = data_matrix_to_string(gadget_borrow)
        write_data(new_gadget,"gadget.csv")
        write_data(new_gadget_borrow,"gadget_borrow_history.csv")
        run = False
        
    elif action == "balikkin gadget":
        balikin_history = []
        balikin_gadget()
        new_gadget = data_matrix_to_string(gadget_list)
        if (balikin_history != []):
            gadget_return.append(balikin_history)
        new_gadget_return = data_matrix_to_string(gadget_return)
        write_data(new_gadget,"gadget.csv")
        write_data(new_gadget_return,"gadget_return_history.csv")
        run = False
        
    elif action == "minta consumable":
        consumable_sejarah = []
        minta_consumables()
        new_consumable = data_matrix_to_string(consumable_list)
        if (consumable_sejarah != []): 
            consumable_history.append(consumable_sejarah)
        new_consumable_history = data_matrix_to_string(consumable_history)
        write_data(new_consumable,"consumable.csv")
        write_data(new_consumable_history,"consumable_history.csv")
        run = False
        
    elif action == "exit":
        run = False

#Test buat bikin history lelellelelelle YAY BISA        
test = ["C90", "Ayam Goreng", "Apakek terserah", 50, "S"]

# gadget_borrow.append(pinjam_history)
# gadget_return.append(balikin_history)
# new_gadget = data_matrix_to_string(gadget_list)
# new_consumable = data_matrix_to_string(consumable_list)
# new_gadget_borrow = data_matrix_to_string(gadget_borrow)
# new_gadget_return = data_matrix_to_string(gadget_return)
# new_consumable_history = data_matrix_to_string(consumable_history)

# write_data(new_gadget,"gadget.csv")
# write_data(new_consumable,"consumable.csv")
# write_data(new_gadget_borrow,"gadget_borrow_history.csv")
# write_data(new_gadget_return,"gadget_return_history.csv")
# write_data(new_consumable_history,"consumable_history.csv")

