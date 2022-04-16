# nilai = int(input("Masukan angkanya: "))
# if nilai <= 10:
#         print("Benar nilanya")
#         flag = True
# else:
#         print("Angka salah")
#         flag = False
# print(flag)

# user = int(input("Masukan angka: "))
# i = 0
# ress = 0
# while i <= user:
#     ress = ress + 1
#     i += 1
# print("Hasilnya adalah", ress)

from email.headerregistry import Address
from multiprocessing import connection
import socket


SRV_ADDR = input("Masukan server ip: ")
SRV_PORT = input("Masukan server port: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
connection, address = s.accept()
print('Client Connected with address: ', address)
while 1:
    data = connection.recv(1024)
    if not data: break
    connection.sendall(b'--Message Received--\n')
    print(data.decode('utf-8'))
connection.close