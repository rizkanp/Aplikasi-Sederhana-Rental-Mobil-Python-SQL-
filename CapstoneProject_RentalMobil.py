# NAMA : RIZKA NUR PRATAMA
# CAPSTONE PROJECT BASIC PROGRAMMING DS PURWADHIKA


# CONNECT TO SQL
## pastikan sebelumnya telah membuat database sesuai yang akan digunakan
## code create database ada di file Rental_Mobil.sql
import mysql.connector

conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "Rizka12012000@",
    database = "rental"
)

print(conn)

koneksi = conn.cursor()

# MENU UTAMA
Menu_Utama = True
while Menu_Utama:
    print("===")
    print("RENTAL MOBIL RIZKA")
    print("1. Show Mobil") #read
    print("2. Tambah Mobil") #create
    print("3. Update Mobil") #update
    print("4. Delete Mobil") #delete
    print("5. Exit")
    print("===")

    Input_Menu_Utama = int(input("Masukkan pilihan anda:"))

# SHOW MOBIL -- READ
    if (Input_Menu_Utama == 1):
        A= True
        while A:
            # Input menu show data
            print("======================")
            print("1. Tampilkan seluruh data")
            print("2. Cari data mobil")
            print("3. Kembali ke menu utama")
            print("======================")

            Input_A = int(input("Masukkan pilihan anda:"))

            #Menampilkan seluruh data di tabel mobil
            if (Input_A == 1):
                koneksi.execute("select * from mobil")
                myresult = koneksi.fetchall()
                mobil = None
                for x in myresult:
                    mobil = x
                    print("Nama_mobil,Warna_mobil,Harga_mobil,Sopir,Plat_Nomor")
                    #Menampilkan seluruh data jika terdapat data di tabel mobil
                    if (mobil != None ):            
                        print(mobil)
                    #Tidak ada data di tabel mobil
                    else:
                        print("TIDAK ADA DATA")

            #Menampilkan data berdasarkan User Input Primary-key
            elif (Input_A == 2):
                Plat_Nomor = input("Plat Nomor:")
                koneksi.execute("select * from mobil where Plat_Nomor = "+Plat_Nomor+" LIMIT 1")
                myresult = koneksi.fetchall()
                Plat_Nomor: None            
                for x in myresult:
                    Plat_Nomor = x
                    print("Nama_mobil,Warna_mobil,Harga_mobil,Sopir,Plat_Nomor")
                    #Menampilkan data yang dicari user
                    if (Plat_Nomor != None):
                        print(x)
                    #Tidak ada data yang dicari user
                    else:
                        print("TIDAK ADA DATA")

            #Back to Menu Utama
            elif(Input_A == 3):
                checker = input ("Apakah anda yakin untuk kembali ke menu utama? (ya/tidak)")
                if (checker == "ya"):
                    break
            
            #Break while (Kembali ke menu A. INPUT SHOW DATA)
            else:
                break


# TAMBAH MOBIL -- CREATE
    if (Input_Menu_Utama == 2):
        B = True
        while B:
            #Input menu create data mobil
            print("======================")
            print("1. Tambahkan data")
            print("2. Kembali ke menu utama")
            print("======================")
            
            Input_B = int(input("Masukkan pilihan anda:"))

            #Menambah data mobil
            if (Input_B == 1):
                Plat_Nomor = input("Plat Nomor:")
                koneksi.execute("select * from mobil where Plat_Nomor = "+Plat_Nomor+" LIMIT 1")
                myresult = koneksi.fetchall()
                mobil = None
                for x in myresult:
                    mobil = x
                #Data duplicate
                if (mobil != None ):
                    print("Data sudah ada")
                #Menambahkan data (Non duplicate data)
                else:
                    Nama_mobil = input ("Nama mobil: ")
                    Warna_mobil = input ("Warna mobil: ")
                    Harga_mobil = int(input("Harga mobil:"))
                    Sopir = input ("Sopir:")
                    Plat_Nomor = input("Plat Nomor:")                    
                    val = (Nama_mobil,Warna_mobil,Harga_mobil,Sopir,Plat_Nomor)
                    print(val)                    
                    #Menambahkan menu pilihan simpan data
                    checker = input ("Apakah anda ingin menyimpan data? (ya/tidak)")
                    if (checker == "ya"):
                        sql = "INSERT INTO mobil (Nama_mobil,Warna_mobil,Harga_mobil,Sopir,Plat_Nomor) VALUES (%s, %s, %s, %s, %s)"                   
                        koneksi.execute(sql, val)
                        conn.commit() 
                        print(koneksi.rowcount,"Data mobil berhasil ditambahkan")       

            #Back to menu utama
            elif(Input_B == 2):
                checker = input ("Apakah anda yakin untuk kembali ke menu utama? (ya/tidak)")
                if (checker == "ya"):
                   break
            
            #Break while (Kembali ke menu B. INPUT CREATE DATA)
            else:
                break


# UPDATE MOBIL -- 
    if (Input_Menu_Utama == 3):
        C = True
        while C:
            #Input menu update data mobil
            print("======================")
            print("1. Update data")
            print("2. Kembali ke menu utama")
            print("======================")
            
            Input_C = int(input("Masukkan pilihan anda:"))

            #Menampilkan pilihan untuk update data (user input primary-key)
            if (Input_C == 1):
                Plat_Nomor = input("Plat Nomor:")
                koneksi.execute("select * from mobil where Plat_Nomor = "+Plat_Nomor+" LIMIT 1")
                myresult = koneksi.fetchall()
                mobil = None
                for x in myresult:
                    mobil = x
                #Menampilkan data yang dicari sesuai primary-key
                if (mobil != None ):
                    print("Nama_mobil,Warna_mobil,Harga_mobil,Sopir,Plat_Nomor")  
                    print(mobil)
                    checker = input ("Apakah anda ingin update data diatas? (ya/tidak)")
                    #Menampilkan pilihan apakah ingin lanjut update data
                    if (checker == "ya"):
                        Nama_mobil = input ("Nama mobil: ")
                        Warna_mobil = input ("Warna mobil: ") 
                        Harga_mobil = input ("Harga mobil: ") 
                        Sopir = input ("Sopir: ")
                    #Menampilkan data yang akan di-update    
                        print("Nama_mobil,Warna_mobil,Harga_mobil,Sopir,Plat_Nomor") 
                        val = (Nama_mobil,Warna_mobil,Harga_mobil,Sopir,Plat_Nomor)
                        print(val)
                    #Menampilkan pilihan apakah ingin melakukan update sesuai data yang ditampilkan diatas
                        update_data = input("Apakah anda yakin untuk update data diatas? (ya/tidak)")
                        if (update_data == "ya"):
                            sql = "UPDATE mobil SET Nama_mobil=%s,Warna_mobil=%s,Harga_mobil=%s, Sopir=%s  WHERE Plat_Nomor=%s"
                            val = (Nama_mobil,Warna_mobil,Harga_mobil,Sopir,Plat_Nomor)
                            print("Data terupdate")
                    else:
                       ("")
                #Data yang dicari tidak ada      
                elif(mobil == None ):
                    print("Data yang anda cari tidak ada")

            #Back to menu utama
            elif(Input_C == 2):
                checker = input ("Apakah anda yakin untuk kembali ke menu utama? (ya/tidak)")
                if (checker == "ya"):
                   break
            
            #Break while (Kembali ke menu C. INPUT UPDATE DATA)
            else:
                break    
            

# DELETE MOBIL
    if (Input_Menu_Utama == 4):
        D = True
        while D:
            #Input data delete data tabel mobil
            print("======================")
            print("1. Hapus data")
            print("2. Kembali ke menu utama")
            print("======================")
            
            Input_D = int(input("Masukkan pilihan anda:"))

            #Menampilkan pilihan untuk delete data (user input primary-key)
            if (Input_D == 1):
                Plat_Nomor = input("Plat Nomor:")
                koneksi.execute("select * from mobil where Plat_Nomor = "+Plat_Nomor+" LIMIT 1")
                myresult = koneksi.fetchall()
                mobil = None
                for x in myresult:
                    mobil = x
                #Menampilkan data yang dicari sesuai dengan primary-key
                if (mobil != None ):
                    print(mobil)
                    #Menampilkan pilihan apakah data diatas akan dihapus
                    checker = input ("Apakah anda ingin menghapus data? (ya/tidak)")
                    if (checker == "ya"):
                        print("Delete data mobil:", mobil)
                        sql = "DELETE FROM mobil WHERE Plat_nomor = "+Plat_Nomor+""
                        koneksi.execute(sql)
                        conn.commit()
                        print(koneksi.rowcount,"Data Deleted")
                    else:
                        ()
                #Data tidak ditemukan
                else:
                    print("Data tidak ditemukan")
                    
            #Back to menu utama
            elif(Input_D == 2):
                checker = input ("Apakah anda yakin untuk kembali ke menu utama? (ya/tidak)")
                if (checker == "ya"):
                   break

            #Break while (Kembali ke menu D. INPUT DELETE DATA)
            else:
                break


# BACK TO MENU UTAMA/KELUAR MENU  
    elif (Input_Menu_Utama == 5):
        checker = input ("Apakah anda yakin untuk keluar dari menu? (ya/tidak)")
        if (checker == "ya"):
            print("TERIMA KASIH!")
            break

# USER SALAH INPUT PILIHAN   
    else:
        print("=====")
        print("PILIHAN YANG ANDA MASUKKAN SALAH")
        print("=====")




