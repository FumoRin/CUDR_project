import sqlite3 as sql
import os
import time
import sys

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
    tempat_duduk = input("Masukkan nomor tempat duduk penumpang :")
    perjalanan = input("Masukkan perjalanan yang akan dilewati : ")
    c.execute("INSERT INTO perjalanan (penumpang, kereta, gerbong, duduk, perjalanan) VALUES (?, ?, ?, ?, ?)", (nama, kereta, gerbong, tempat_duduk, perjalanan))
    conn.commit()
    print("Penumpang sudah ditambahkan sudah ditambahkan! \n")

def hapus_penumpang():
    clear()
    id = input("Masukkan nomor ID penumpang yang akan Dibatalkan : ")
    c.execute("DELETE FROM perjalanan WHERE id = ?", (id,))
    conn.commit()
    print("Penumpang sudah dibatalkan dari database! \n")

def edit_penumpang():
    clear()
    id = input("Masukkan nomor ID penumpang yang akan diubah : ")
    nama = input("Masukkan nama penumpang yang baru : ")
    kereta = input("Masukkan nama kereta yang baru : ")
    gerbong = input("Masukkan bagian gerbong yang baru : ")
    tempat_duduk = input("Masukkan nomor tempat duduk yang baru : ")
    perjalanan = input("Masukkan perjalanan baru yang diinginkan : ")
    c.execute("UPDATE perjalanan SET (penumpang=?, kereta=?, gerbong=?, duduk=?, perjalanan=?)", (nama, kereta, gerbong, tempat_duduk, perjalanan))
    conn.commit()
    print("Perubahan sudah dibuat di database!")

def read_all():
    c.execute("SELECT * FROM perjalanan")
    return c.fetchall()

def read_specific(id):
    c.execute("SELECT * FROM perjalanan WHERE id=?", (id,))
    return c.fetchall()

def read_info():
    clear()
    id = input("Masukkan ID penumpang yang ingin ditampilkan (Kosongkan jika ingin melihat semua data penumpang) : ")
    penumpang = read_all() if not id else read_specific(id)
    if not penumpang:
        clear()
        print("ID yang dimasukkan tidak ada di database, Coba cek kembali ID penumpang yang dimasukkan.")
    else :
        for penumpang in penumpang:
            clear()
            print(f"ID = {penumpang[0]}, Nama Penumpang = {penumpang[1]}, Kereta = {penumpang[2]}, Gerbong = {penumpang[3]}, Tempat Duduk = {penumpang[4]}, Perjalanan = {penumpang[5]}")

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
    os.system("cls")

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

        repeat = input("Apakah anda ingin menggunakan kembali program ini? (yes/no) : ".lower())
        if repeat != "yes":
            loadingOut()
            clear()
            break

    
        
    




if __name__ == '__main__':
    main_program()
