from tkinter import *
from tkinter import messagebox
from datetime import datetime

#"""
#  .\ngrok config add-authtoken 3DWrwqqcuSm3Jvzbrkj5N6qDPCG_7TMwWYGh4rrbg9oQmdbcx
#أمر تشغيل السيرفر المعالمي
#أمر تشغيل السيرفر المعالمي
#PS C:\Users\AL> .\ngrok.exe http 4040

#"""

# ==============================
# إعداد النافذة
# ==============================

root = Tk()
root.title("Secure Chat")
root.geometry("350x550")
root.minsize(350, 550)
root.configure(bg="#1e1e1e")
# نخلي الشبكة تتمدد صح
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# ==============================
# القائمة العلوية
# ==============================

menu_bar = Menu(root)

# قائمة ملف
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="خروج", command=root.quit)

menu_bar.add_cascade(label="ملف", menu=file_menu)

# قائمة معلومات
info_menu = Menu(menu_bar, tearoff=0)

info_menu.add_command(
    label="من نحن",
    command=lambda: messagebox.showinfo(
        "من نحن",
        "مشروع دردشة مطور باستخدام Python و Tkinter"
    )
)

info_menu.add_command(
    label="فكرة المشروع",
    command=lambda: messagebox.showinfo(
        "فكرة المشروع",
        "برنامج دردشة احترافي سيتم تطويره للإرسال عبر الإنترنت"
    )
)

menu_bar.add_cascade(label="معلومات", menu=info_menu)

root.config(menu=menu_bar)

# ==============================
# عنوان أعلى الشات
# ==============================

header = Label(
    root,
    text="Secure Chat",
    bg="#2b2b2b",
    fg="white",
    font=("Arial", 16, "bold"),
    pady=10
)

header.pack(fill=X)

# ==============================
# مربع الرسائل
# ==============================

chat_box = Text(
    root,
    bg="#252526",
    fg="white",
    font=("Arial", 11),
    relief=FLAT,
    wrap=WORD,
    padx=10,
    pady=10
)

chat_box.pack(expand=True, fill=BOTH, padx=10, pady=10)

# ألوان الرسائل
chat_box.tag_config(
    "user",
    foreground="white",
    background="#0084ff",
    spacing1=5,
    spacing3=5
)

chat_box.tag_config(
    "bot",
    foreground="black",
    background="#e5e5ea",
    spacing1=5,
    spacing3=5
)

# ==============================
# الإطار السفلي
# ==============================

bottom_frame = Frame(root, bg="#1e1e1e")
bottom_frame.pack(fill=X, padx=10, pady=10)


# مربع الإدخال
entry = Entry(
    bottom_frame,
    font=("Arial", 12),
    relief=FLAT
)

entry.pack(side=LEFT, fill=X, expand=True, ipady=10, padx=(0, 10))

entry.focus_set()

# ==============================
# دالة الإرسال
# ==============================

def send_message():

    message = entry.get()

    if message.strip() != "":

        time_now = datetime.now().strftime("%H:%M")

        # رسالة المستخدم
        chat_box.insert(
            END,
            f"\nأنت [{time_now}]\n{message}\n",
            "user"
        )

        entry.delete(0, END)

        # رد تجريبي
        bot_reply = f"وصلت رسالتك: {message}"

        time_now = datetime.now().strftime("%H:%M")

        chat_box.insert(
            END,
            f"\nصديق [{time_now}]\n{bot_reply}\n",
            "bot"
        )

        # النزول لآخر رسالة
        chat_box.see(END)

# ==============================
# زر الإرسال
# ==============================

send_button = Button(
    bottom_frame,
    text="إرسال",
    command=send_message,
    bg="#0084ff",
    fg="white",
    activebackground="#006fd6",
    activeforeground="white",
    relief=FLAT,
    font=("Arial", 11, "bold"),
    padx=20,
    pady=8,
    cursor="hand2"
)

send_button.pack(side=RIGHT)

# إرسال بـ Enter
entry.bind("<Return>", lambda event: send_message())

# ==============================
# تشغيل البرنامج
# ==============================

root.mainloop()