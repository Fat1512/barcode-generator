import barcode
from barcode.writer import ImageWriter
import random

# data = '213241235212'
# data1 = str(data)
#
# a = barcode.get_barcode_class('upc')
# b = a(data1, writer=ImageWriter)
# c = b.save('data/barcode_{product_id}'.format(product_id=1))

data = str(random.randint(100000000000,999999999999))
barcode_class = barcode.get_barcode_class('upc')
b = barcode_class(data, writer=ImageWriter)
b.save('data/barcode_{product_id}'.format(product_id=2))