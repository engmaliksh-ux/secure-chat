import socket

#"""
#  .\ngrok config add-authtoken 3DWrwqqcuSm3Jvzbrkj5N6qDPCG_7TMwWYGh4rrbg9oQmdbcx
#أمر تشغيل السيرفر المعالمي
#أمر تشغيل السيرفر المعالمي
#PS C:\Users\AL> .\ngrok.exe http 4040
#"""

# الاتصال بالسيرفر
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.0.101"
port = 12345

client.connect((host, port))

print("Connected to server!")

while True:

    message = input("You: ")

    client.send(message.encode())

    reply = client.recv(1024).decode()

    print("Friend:", reply)