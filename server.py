import socket
import os


# إنشاء السيرفر
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP + PORT
host = "0.0.0.0"
port = int(os.environ.get("PORT", 12345))

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