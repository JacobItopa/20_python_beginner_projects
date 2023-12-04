import qrcode

def qrcode_generator(url):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 20,
        border = 8,
    )

    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#008080", back_color="white")
    img.save("patakiconsulting005.png")

url = input("Please input a url you would like to conxert to a qrcode: ")
qrcode_generator(url)