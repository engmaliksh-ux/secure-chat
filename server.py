"""
import socket
import os

host = "0.0.0.0"
port = int(os.environ.get("PORT", 12345))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((host, port))

server.listen()

print("Server started... Waiting for connections")

while True:
    client, address = server.accept()

    print(f"Connected with: {address}")

    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print("Client:", message)

            reply = f"Server received: {message}"

            client.send(reply.encode())

        except:
            break

    client.close()

    print("Connection closed")
"""

import socket
import os


# IP + PORT
host = "0.0.0.0"
port = int(os.environ.get("PORT", 12345))

# إنشاء السيرفر
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ربط السيرفر
server.bind((host, port))

# تشغيل الاستماع
server.listen()

print("Server started... Waiting for connection")

# انتظار اتصال
client_socket, client_address = server.accept()

print(f"Connected with: {client_address}")

# استقبال وإرسال رسائل
while True:
    try:
        msg = client_socket.recv(1024).decode()
        if not msg:
            break

        print("Friend:", msg)

        reply = input("You: ")
        client_socket.send(reply.encode())

    except:
        print("Connection closed by client")
        break

client_socket.close()

