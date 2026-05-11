from tkinter import *
from datetime import datetime
import socket
import threading

# =========================
# الاتصال بالسيرفر
# =========================

host = "127.0.0.1"
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# =========================
# واجهة البرنامج
# =========================

root = Tk()
root.title("Secure Chat")
root.geometry("500x600")

# مربع الشات
chat_box = Text(root, bg="#1e1e1e", fg="white", font=("Arial", 11))
chat_box.pack(expand=True, fill=BOTH)

# إطار سفلي
bottom_frame = Frame(root)
bottom_frame.pack(fill=X)

entry = Entry(bottom_frame, font=("Arial", 12))
entry.pack(side=LEFT, fill=X, expand=True, padx=5, pady=5)

entry.focus_set()

# =========================
# إرسال الرسائل
# =========================

def send_message():

    message = entry.get()

    if message.strip() != "":

        time_now = datetime.now().strftime("%H:%M")

        chat_box.insert(
            END,
            f"\nأنت [{time_now}]: {message}\n"
        )

        client.send(message.encode())

        entry.delete(0, END)

        chat_box.see(END)

# =========================
# استقبال الرسائل
# =========================

def receive_messages():

    while True:

        try:

            message = client.recv(1024).decode()

            time_now = datetime.now().strftime("%H:%M")

            chat_box.insert(
                END,
                f"\nصديق [{time_now}]: {message}\n"
            )

            chat_box.see(END)

        except:
            break

# Thread للاستقبال
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# زر الإرسال
button = Button(
    bottom_frame,
    text="إرسال",
    command=send_message
)

button.pack(side=RIGHT, padx=5)

# Enter
entry.bind("<Return>", lambda event: send_message())

# تشغيل
root.mainloop()