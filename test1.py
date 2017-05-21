import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('file:///Users/pro/Desktop/love/index.html')
qr.make(fit=True)
img = qr.make_image()
img.save("qrcode_demo.png")