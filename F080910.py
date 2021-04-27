#Meminjam gadget
import os
import sys
import math
import time 
import argparse
import datetime


#F08 Pinjam gadget
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
        
#F09 Balikkin gadget
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

#F10 Minta consumable
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

#buat terminal
run = True
load_data()

while run: 
    action = str(input("mau ngapain?? "))
    
    if action == "pinjam":
        pinjam_history = []
        pinjam_gadget()
        if (pinjam_history != []):
            gadget_borrow_history_matrix.append(pinjam_history)
        gadget_matrix_string = data_matrix_to_string(gadget_matrix)
        gadget_borrow_history_matrix_string = data_matrix_to_string(gadget_borrow_history_matrix)
        
        
    elif action == "balikkin":
        balikin_history = []
        balikin_gadget()
        if (balikin_history != []):
            gadget_return_history_matrix.append(balikin_history)
        gadget_matrix_string = data_matrix_to_string(gadget_matrix)
        gadget_return_history_matrix_string = data_matrix_to_string(gadget_return_history_matrix)
        gadget_borrow_history_matrix_string = data_matrix_to_string(gadget_borrow_history_matrix)
        
        
    elif action == "minta":
        consumable_sejarah = []
        minta_consumables()
        if (consumable_sejarah != []): 
            consumable_history_matrix.append(consumable_sejarah)
        consumable_matrix_string = data_matrix_to_string(consumable_matrix)
        consumable_history_matrix_string = data_matrix_to_string(consumable_history_matrix)
