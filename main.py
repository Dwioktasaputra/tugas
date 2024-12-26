from koneksiDB import * 
from pegawai import *

#buat objek koneksi
dbku = MyDB()
conn_dbku, cur_dbku = dbku.connect()

#buat objek pegawai1, set connection dan cursor yang diambil nilainya dari objek dbku
tbl_pegawai = Pegawai(conn=conn_dbku, cursor=cur_dbku)

#menambahkan data pada tabel pegawai
tbl_pegawai.tambah('12', 'Andik', 'Batam Center', 'andik@uib.ac.id')
