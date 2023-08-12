import qrcode

my_qr_code = qrcode.make('https://pypi.org/project/qrcode/')
type(my_qr_code)
my_qr_code.save('image_qrcode3.png')