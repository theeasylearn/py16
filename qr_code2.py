import qrcode

my_qrcode = qrcode.QRCode()
my_qrcode.add_data('https://pypi.org/project/qrcode/')
my_qrcode.make(fit=True)
image = my_qrcode.make_image(fill_color='yellow',back_color='black')
image.save('image_qrcode4.png')