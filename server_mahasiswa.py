#!/usr/bin/python3

# Made by :
# - Ananda Adiyatma Putra
# - Satria Adhi Kharisma

from flask import Flask, request, jsonify
import json

app = Flask("Web App Mahasiswa")

data_mahasiswa = [
    {
        "nim" : 123,
        "nama" : "Andi"
    },
    {
        "nim" : 234,
        "nama" : "Budi"
    }
]

@app.route('/mahasiswa', methods=['GET'])
def get_all_mahasiswa():
    json_mahasiswa = json.dumps(data_mahasiswa)
    return json_mahasiswa

@app.route('/mahasiswa', methods=['POST'])
def create_mahasiswa():
    # Dapatkan data nim dan nama dari body request
    nim = request.json['nim']
    nama = request.json['nama']
    # Buat data mahasiswa baru
    mahasiswa_baru = {
        "nim" : nim,
        "nama" : nama
    }
    # Tambahkan ke list data mahasiswa
    data_mahasiswa.append(mahasiswa_baru)
    # Return OK
    return "OK"

@app.route('/mahasiswa', methods=['DELETE'])
def delete_mahasiswa():
    # Dapatkan data nim dan nama dari body request
    nim = request.json['nim']
    nama = request.json['nama']
    # Delete data mahasiswa
    mahasiswa_del = {
        "nim" : nim,
        "nama" : nama
    }
    # Tambahkan ke list data mahasiswa
    data_mahasiswa.remove(mahasiswa_del)
    # Return OK
    return "OK"

@app.route('/mahasiswa/<int:id>', methods=['GET'])
def get_satu_mahasiswa(id):
    json_mahasiswa = [data_mahasiswa for data_mahasiswa in data_mahasiswa if data_mahasiswa['nim'] == id]
    return jsonify({'mahasiswa' : json_mahasiswa[0]})

@app.route('/mahasiswa/<int:id>', methods=['PUT'])
def update_mahasiswa(id):
    data = [ dt for dt in data_mahasiswa if (dt['nim'] == id)]
    if 'nim' in request.json :
        data[0]['nim'] = request.json['nim']
    if 'nama' in request.json :
        data[0]['nama'] = request.json['nama']
    return jsonify({'dt' :data[0]})



app.run(port=7777)
