import barcode
from barcode import EAN13

data = '1224234234123'
my_code = EAN13(data)
# my_code.save("myBarCode")
x = my_code.render()
print(x)