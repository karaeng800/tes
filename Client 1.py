import socket
import threading
import time
HOST = '149.129.239.105'
PORT = 50001

#HOST = '127.0.0.1'  
#PORT = 10000  

def auth(client_socket):
    b = b'\x03\x00\x00L\x03\x00\x00\x00\xa0\xff\x00\x00\x00\x00\x00\x00'
    b += b'\xeb\xd5\x93\x0b\x00\x00\x00\x006cb88b08'
    b += b'464a2400\x00\x00\x00\x00\x00\x00\x00\x00'
    b += b'\x00\x00\x00\x00\x00\x00\x00\x00V1.01\x00\x00\x00'
    b += b'\x00\x00\x00\x00\x00`\x01\x00\x02\x00\x00\x00'
    client_socket.send(b)
    data = client_socket.recv(1024)
    print('Received', repr(data))

def client_program(client_socket):
    #message = input(" -> ")  # take input
    #while message.lower().strip() != 'exit':
    while True:
        time.sleep(0.3)
        #BasicSPin180
        #bs = b'\x03\x00\x00 \x03\x00\x00\x00\x11\xa0\x00\x00\x00\x00\x00\x00'
        #bs += b"\x00\x00\x00\x00\x01\x00\x00\x00\x12\x00\x00\x00\x10'\x00\x00"

        #BasicSPin80
        bs = b'\x03\x00\x00 \x03\x00\x00\x00\x11\xa0\x00\x00\x00\x00\x00\x00'
        bs += b"\x00\x00\x00\x00\x01\x00\x00\x00\x08\x00\x00\x00\x10'\x00\x00"

        #BasicSPin1760
        #bs += b'\x03\x00\x00 \x03\x00\x00\x00\x11\xa0\x00\x00\x00\x00\x00\x00'
        #bs += b"\x00\x00\x00\x00\x02\x00\x00\x00X\x00\x00\x00\x10'\x00\x00"
        
        #BasicSPin4400
        #bs += b'\x03\x00\x00 \x03\x00\x00\x00\x11\xa0\x00\x00\x00\x00\x00\x00'
        #bs += b"\x00\x00\x00\x00\x05\x00\x00\x00X\x00\x00\x00\x10'\x00\x00"

        #FreeGame80
        #bs = b'\x03\x00\x00 \x03\x00\x00\x00\x11\xa0\x00\x00\x00\x00\x00\x00'
        #bs += b"\x01\x00\x00\x00\x01\x00\x00\x00\x08\x00\x00\x00\x10'\x00\x00"
        
        #FreeGame17
        #bs = b'\x03\x00\x00 \x03\x00\x00\x00\x11\xa0\x00\x00\x00\x00\x00\x00'
        #bs += b"\x01\x00\x00\x00\x0f\x00\x00\x00X\x00\x00\x00\x10'\x00\x00"
        
        #FreeGame13
        #bs = b'\x03\x00\x00 \x03\x00\x00\x00\x11\xa0\x00\x00\x00\x00\x00\x00'
        #bs += b"\x01\x00\x00\x00\x0f\x00\x00\x00X\x00\x00\x00\x10'\x00\x00"

        client_socket.send(bs)  # send message
        data = client_socket.recv(1024)
        print('Received', repr(data))
        #message = input(" -> ")  # again take input
    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_socket = socket.socket()  # instantiate
    client_socket.connect((HOST, PORT))  # connect to the server
    auth(client_socket)
    #client_program(client_socket)
    N = 1
    threads = [threading.Thread(target=client_program, args=[client_socket]) for i in range(N)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

