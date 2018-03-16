#!/usr/bin/python3

# Made by :
# - Ananda Adiyatma Putra
# - Satria Adhi Kharisma

import http.client
import json

ip_server = "127.0.0.1"
port_server = 7777

def get_mahasiswa():
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    # Kirim request ke server
    conn.request("GET", "/mahasiswa")
    # Baca responsenya
    data = conn.getresponse().read()
    data = data.decode('ascii')
    print(data)

def add_mahasiswa():
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    # Definisi headers HTTP
    header = {"Content-Type" : "application/json"}
    # Definisikan data yang akan ditambahkan
    mhs = {
        "nim" : 910,
        "nama" : "Eka"
    }
    json_mhs = json.dumps(mhs)
    # Kirim request POST /mahasiswa dengan body dan header
    conn.request("POST", "/mahasiswa", json_mhs, header)
    # Baca responsenya
    data = conn.getresponse().read()
    data = data.decode('ascii')
    print(data)

def del_mahasiswa():
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    # Definisi headers HTTP
    header = {"Content-Type" : "application/json"}
    # Definisikan data yang akan dihapus
    mhs = {
        "nim" : 123,
        "nama" : "Andi"
    }
    json_mhs = json.dumps(mhs)
    # Kirim request DELETE /mahasiswa dengan body dan header
    conn.request("DELETE", "/mahasiswa", json_mhs, header)
    # Baca responsenya
    data = conn.getresponse().read()
    data = data.decode('ascii')
    print(data)

def get_mahasiswabyid(id):
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    # Kirim request ke server
    conn.request("GET", "/mahasiswa/"+str(id))
    # Baca responsenya
    data = conn.getresponse().read()
    data = data.decode('ascii')
    print(data)

def update_mahasiswa(id):
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    # Kirim request ke server
    header = {"Content-Type": "application/json"}
    mhs = {
        "nim" : 222,
        "nama" : "santi"
    }
    json_mhs = json.dumps(mhs)
    conn.request("PUT", "/mahasiswa/"+str(id), json_mhs, header )

    data = conn.getresponse().read()
    data = data.decode('ascii')
    print(data)

#Panggil fungsi
#untuk mencoba jalankan satu per satu sesuai kebutuhan
#add_mahasiswa()
#del_mahasiswa()
#get_mahasiswa()
#get_mahasiswabyid(234)
#update_mahasiswa(123)
