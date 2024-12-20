import barcode
from barcode.writer import ImageWriter
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Double, DATETIME
import random

app = Flask(__name__)
app.secret_key = "8923yhr9fuwnsejksnpok@$I_I@$)opfk"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:151204@localhost/book_store'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)


class Book(db.Model):
    __tablename__ = 'book'
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    quantity = Column(Integer)
    price = Column(Double)
    description = Column(String)
    release_date = Column(DATETIME)
    num_page = Column(Integer)
    dimension = Column(String)
    weight = Column(Double)
    barcode = Column(String)
    format = Column(String)


@app.route("/")
def go():
    books = Book.query.all()
    for book in books:
        upc_base = [random.randint(0, 9) for _ in range(11)]

        # Calculate the check digit
        odd_sum = sum(upc_base[i] for i in range(0, 11, 2))
        even_sum = sum(upc_base[i] for i in range(1, 11, 2))
        total_sum = odd_sum * 3 + even_sum
        check_digit = (10 - (total_sum % 10)) % 10

        upc_base.append(check_digit)
        data = ''.join(map(str, upc_base))
        barcode_class = barcode.get_barcode_class('upc')

        b = barcode_class(data, writer=ImageWriter)
        b.save('data/barcode_{product_id}_{barcode}'.format(product_id=book.book_id,barcode=data))
        book.barcode = data
    db.session.commit()
    return "!2"
if __name__ == "__main__":
    app.run(debug=True)

# data = '213241235212'
# data1 = str(data)
#
# a = barcode.get_barcode_class('upc')
# b = a(data1, writer=ImageWriter)
# c = b.save('barcode')
