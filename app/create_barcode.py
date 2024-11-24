import barcode
from barcode.writer import ImageWriter


data='213241235212'
data1=str(data)

a = barcode.get_barcode_class('upc')
b = a(data1, writer = ImageWriter)
c = b.save('barcode')