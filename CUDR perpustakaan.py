import sqlite3
import time

def open_database(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    return conn, c

def create_database(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE isi_database 
    (id INTEGER PRIMARY KEY,
    nama TEXT,
    pengarang TEXT,
    waktu INTEGER)''')
    conn.commit()
    conn.close()
    print(f"Database {db_name} telah berhasil dibuat")

def add_buku(db_name):
    nama = input("Masukkan nama buku yang dimasukkan : ")
    pengarang = input("Masukkan nama pengarang buku: ")
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    waktu = int(time.time())
    c.execute("INSERT INTO isi_database (nama, pengarang, waktu) VALUES(?,?,?)", (nama, pengarang, waktu))
    conn.commit()
    conn.close()

    print(f" Buku ", {nama}, " telah dimasukkan ke dalam database")


def delete_buku(db_name):
    nama = input("Masukkan nama buku yang akan dihapus")
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("DELETE FROM isi_database WHERE nama=?", (nama,))
    conn.commit()
    conn.close

def update_buku(db_name):
    nama = input("Masukkan nama buku yang akan diperbarui :")
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM isi_database WHERE nama=?", (nama,))
    buku = c.fetchone()
    if buku is None:
        print(f"Buku {nama} tidak ditemukan di database")
    else:
        new_nama = input(f"Masukkan nama buku baru untuk {nama} :")
        new_pengarang = input(f"Masukkan nama buku baru untuk nama pengarang :")
        new_waktu = int(time.time())
        c.execute("UPDATE isi_database set nama=?, pengarang=?, waktu=?", (new_nama, new_pengarang, new_waktu))
        conn.commit()
        conn.close()
        
def list_buku(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * WHERE isi_database")
    buku = c.fetchall()
    print("Berikut merupakan list buku yang terdapat di dalam database :")
    for isi in buku:
        waktu = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(buku[4]))
        print(f"Buku : {isi[1]} \nPengarang : {isi[2]} \nWaktu didaftarkan : {isi[3]}")
    conn.close()

def main_program():
    db_name = input("Masukkan nama database yang ingin dibuka :")
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Check if the "people" table already exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='people'")
    table_exists = c.fetchone()

    if table_exists is not None:
        open_database(db_name)
    else:
        create_database(db_name)

    while True:
        print("\n1. Tambahkan buku di database")
        print("2. Hapus buku dari database")
        print("3. Tampilkan semua buku yang ada di database")
        print("4. Keluar Program")
        pilihan = int(input("Masukkan pilihan yang anda inginkan : "))

        if pilihan == 1:
            add_buku(db_name)
        elif pilihan == 2:
            delete_buku(db_name)
        elif pilihan == 3:
            list_buku(db_name)
        elif pilihan == 4:
            break
        else:
            print("Pilihan anda salah. Coba lagi. \n")

    print("Goodbye!")

main_program()

