print("Selamat datang di Inventarisasi Kantong Ajaib milik Doremonangis!")
load_data()
help()
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

            elif action == "tambah item":
                if state == "Admin":
                    tambahitem()
                    loggedOn = True
                else:
                    print("Hanya admin yang dapat menggunakan fitur ini!")

            elif action == "hapus item":
                if state == "Admin":
                    hapusitem()
                    loggedOn = True
                else:
                    print("Hanya admin yang dapat menggunakan fitur ini!")

            elif action == "ubah jumlah":
                if state == "Admin":
                    ubahjumlah()
                    loggedOn = True
                else:
                    print("Hanya admin yang dapat menggunakan fitur ini!")

            elif action == "help":
                help()
                loggedOn = True
                

    elif state == "Not logged in":
        run = True