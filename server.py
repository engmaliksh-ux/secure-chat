import socket

# إنشاء السيرفر
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP + PORT
host = "0.0.0.0"
port = 12345

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

    message = client_socket.recv(1024).decode()

    if not message:
        break

    print("Friend:", message)

    reply = input("You: ")

    client_socket.send(reply.encode())