import pymysql
#variabel cursor global
curr = any
conn = any

class MyDB:    
     def connect(self):
        con = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             database='direktur',
                             )
        cur = con.cursor()
        return cur, con

class Pegawai:
    def __init__(self, cursor, conn):
        self.cur = cursor
        self.conn = conn

    def cari_pegawai(self, id):
        self.cur.execute('SELECT * FROM Pegawai WHERE id_pegawai ='+ id) 
        result = self.cur.fetchall()
        return result

    def tambah (self, id, nama, alamat, email):
        print('Tambah data pegawai...')
        query = 'INSERT INTO Pegawai (id_pegawai, nama, alamat, email) VALUES ("' + id +'","'+ nama +'","'+alamat + '","'+email+'")';
        self.cur.execute(query)      
        self.conn.commit()
        # print('Query:', query)
        print('Proses penambahan selesai')

    def hapus(self, id):
        print('Menghapus data pegawai...')
        query = 'DELETE FROM Pegawai WHERE id_pegawai'
        self.cur.execute(query, (id,))
        self.conn.commit()
        print('Proses penghapusan selesai')
        # print('Query:', query)
        pass

    def update_alamat(self, id, alamat):
        print('Memperbarui alamat pegawai...')
        query = 'UPDATE Pegawai SET (id_pegawai, alamat,) VALUES ("' + id +'","'+ alamat + '",)'
        self.cur.execute(query, (alamat, id))
        self.conn.commit()
        print('Proses pembaruan alamat selesai')
         # print('Query:', query)
        pass
        

class Gaji:

    def hitung_pajak():
        pass

Dbase = MyDB()
curr, conn = Dbase.connect()

#buat object Pegawai
pgw = Pegawai(curr, conn)

# key = input('Silakan masukkan id pegawai yang dicari: ')
# hasil = pgw.cari_pegawai(key)
# print(hasil)

print('*** Silakan memilih menu (1,2) ****')
print('1. Tambah data pegawai \n2. hapus')
menu = input('Menu yang dipilih: ')

if (menu == '1'):
    print('Silakan masukkan data berikut')
    id_pgw = input('id pegawai: ')
    nama = input('nama: ')
    alamat = input('alamat: ')
    em = input('email: ')
    pgw.tambah(id_pgw, nama, alamat, em)

if (menu == '2'):
    id_hapus = input('masukkan id pegawai yang akan dihapus: ')
    pgw.hapus(id_pgw)