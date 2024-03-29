import sqlite3 as sql
import os
import time
import sys
from prettytable import PrettyTable
# Modul diatas harus terinstall. 
# Jika terjadi error karena modul tidak ada, install melalui cmd dengan command "pip install []" atau "python.exe pip install []"

conn = sql.connect('perjalanan.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS perjalanan
            (id INTEGER PRIMARY KEY,
            penumpang TEXT,
            kereta TEXT,
            gerbong TEXT,
            duduk INTEGER,
            perjalanan TEXT)''')

def tambah_penumpang():
    clear()
    nama = input("Masukkan nama penumpang : ")
    kereta = input("Masukkan nama kereta : ")
    gerbong = input ("Masukkan bagian gerbong yang diinginkan : ")
    tempat_duduk = input("Masukkan nomor tempat duduk penumpang : ")
    perjalanan = input("Masukkan perjalanan yang akan dilewati : ")
    c.execute("INSERT INTO perjalanan (penumpang, kereta, gerbong, duduk, perjalanan) VALUES (?, ?, ?, ?, ?)", (nama, kereta, gerbong, tempat_duduk, perjalanan))
    conn.commit()
    print("Penumpang sudah ditambahkan! \n")

def hapus_penumpang():
    clear()
    id = input("Masukkan nomor ID penumpang yang akan Dibatalkan : ")
    c.execute("DELETE FROM perjalanan WHERE id = ?", (id,))
    conn.commit()
    print("Penumpang sudah dibatalkan dari database! \n")

def edit_penumpang():
    clear()
    penumpang = read_all()
    table = PrettyTable()
    table.field_names = ["ID", "Nama Penumpang", "Kereta", "Gerbong", "Tempat Duduk", "Perjalanan"]
    for orang in penumpang:
        table.add_row([orang[0], orang[1], orang[2], orang[3], orang[4], orang[5]])
    print(table)
    id = int(input("Masukkan nomor ID penumpang yang akan diubah : "))
    c.execute("SELECT * FROM perjalanan WHERE id=?", (id,))
    penumpang = c.fetchone()
    if penumpang is None:
        print(f"Penumpang dengan ID {id} tidak ditemukan di database")
    else:
        clear()
        print(f"Data penumpang dengan ID {id} : ")
        print(f"1. Nama Penumpang : {penumpang[1]}")
        print(f"2. Kereta : {penumpang[2]}")
        print(f"3. Gerbong : {penumpang[3]}")
        print(f"4. Tempat duduk : {penumpang[4]}")
        print(f"5. Perjalanan : {penumpang[5]}")

        choice = input("Masukkan data yang anda ingin ubah (1-5) : ")

        while True:
            if choice:
                if choice == "1":
                    nama = input("Masukkan nama penumpang yang baru : ")
                    c.execute("UPDATE perjalanan SET penumpang=? WHERE id=?", (nama, id))
                    conn.commit()
                    clear()
                    print("Data penumpang telah dibuat!")
                    break
                elif choice == "2":
                    kereta = input("Masukkan nama kereta yang baru : ")
                    c.execute("UPDATE perjalanan SET kereta=? WHERE id=?", (kereta, id))
                    conn.commit()
                    clear()
                    print("Data penumpang telah diubah!")
                    break
                elif choice == "3":
                    gerbong = input("Masukkan bagian gerbong yang baru : ")
                    c.execute("UPDATE perjalanan SET gerbong=? WHERE id=?", (gerbong , id))
                    conn.commit()
                    clear()
                    print("Data penumpang telah diubah!")
                    break
                elif choice == "4":
                    tempat_duduk = int(input("Masukkan nomor tempat duduk yang baru : "))
                    c.execute("UPDATE perjalanan SET duduk=? WHERE id=?", (tempat_duduk, id))
                    conn.commit()
                    clear()
                    print("Data penumpang telah diubah!")
                    break
                elif choice == "5":
                    perjalanan = input("Masukkan perjalanan baru yang diinginkan : ")
                    c.execute("UPDATE perjalanan SET perjalanan=? WHERE id=?", (perjalanan, id))
                    conn.commit()
                    clear()
                    print("Data Penumpang telah diubah!")
                    break
                else:
                    print("Pilihan anda tidak valid, Coba kembali.")

def read_all():
    c.execute("SELECT * FROM perjalanan")
    return c.fetchall()

def read_specific(id):
    c.execute("SELECT * FROM perjalanan WHERE id=?", (id,))
    return c.fetchall()

def read_info():
    clear()
    id = input("Masukkan ID penumpang yang ingin ditampilkan (Kosongkan jika ingin melihat semua data penumpang) : ")
    clear()
    penumpang = read_all() if not id else read_specific(id)
    if not penumpang:
        print("ID yang dimasukkan tidak ada di database, Coba cek kembali ID penumpang yang dimasukkan.")
    else :
        table = PrettyTable()
        table.field_names = ["ID", "Nama Penumpang", "Kereta", "Gerbong", "Tempat Duduk", "Perjalanan"]
        for orang in penumpang:
            table.add_row([orang[0], orang[1], orang[2], orang[3], orang[4], orang[5]])
        print(table)

def loadingIn():
    print("Loading :")
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.3)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")

def loadingOut():
    print("Keluar Program :")
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

def clear():
    os.system("cls" if os.name == 'nt' else 'clear')

def main_program():
    clear()  
    print(f"{'='*80}")
    print(f"|{'PROGRAM DATABASE':^78}|")
    print(f"|{'PERJALANAN PENUMPANG ':^78}|")
    print(f"|{'KERETA API ':^78}|")
    print(f"{'='*80}")
    loadingIn()
    
    while True :
        clear()
        print(" Selamat Datang Di Menu Program Perjalanan Penumpang Kereta Api!")
        print(" 1. Tambah Penumpang \n 2. Ubah Info Perjalanan Penumpang \n 3. Pembatalan Perjalanan Penumpang  \n 4. Check Info Perjalanan Penumpang")
        
        while True:
            output = input("Masukkan Pilihan yang Anda Ingin Lakukan : ")
            if output == "1":
                print("\n")
                tambah_penumpang()
                break
            elif output == "2":
                print("\n")
                edit_penumpang()
                break
            elif output == "3":
                print("\n")
                hapus_penumpang()
                break
            elif output == "4":
                print("\n")
                read_info()
                break
            else :
                print("Pilihan yang anda masukkan tidak valid, Mohon untuk coba kembali.")

        repeat = input("Apakah anda ingin menggunakan kembali program ini? (yes/no) (default : no) : ".lower())
        if repeat != "yes":
            loadingOut()
            clear()
            break


if __name__ == '__main__':
    main_program()
