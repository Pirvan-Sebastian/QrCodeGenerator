import customtkinter as ctk
from tkinter import messagebox, Label
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    link = entry.get()
    if not link:
        messagebox.showwarning("Input Error", "Please enter a link")
        return

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=1)
    qr.add_data(link)
    qr.make(fit=True)

    global img, qr_img
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("qrcode.png")

    resize_qr_image()

def resize_qr_image(event=None):
    global img, qr_img
    if qr_img:
        min_dimension = min(root.winfo_width(), root.winfo_height())
        img = qr_img.resize((min_dimension // 2, min_dimension // 2), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)

        qr_label.configure(image=img)
        qr_label.image = img

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("QR Code Generator")

ctk.CTkLabel(root, text="Paste the link:").pack(pady=10)
entry = ctk.CTkEntry(root, width=300)
entry.pack(pady=5)

generate_button = ctk.CTkButton(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=20)

qr_label = Label(root, bg=root.cget("background"))
qr_label.pack(pady=10)

root.bind("<Configure>", resize_qr_image)
root.mainloop()