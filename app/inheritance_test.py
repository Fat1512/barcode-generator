from sqlalchemy.orm import relationship
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Double, DATETIME

app = Flask(__name__)
app.secret_key = "8923yhr9fuwnsejksnpok@$I_I@$)opfk"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:151204@localhost/test_db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)


class Parent(db.Model):
    __tablename__ = 'parent'
    parent_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    child = relationship("Child", backref="parent", lazy=True, uselist=False)


class Child(Parent):
    __tablename__ = 'child'
    parent_id = Column(Integer, ForeignKey('parent.parent_id'), primary_key=True, unique=True)
    age = Column(String(100), primary_key=True)
    birthdate = Column(String(100), primary_key=True)

if __name__ == '__main__':
    with app.app_context():
        c = Child(name="phat", age="12", birthdate="15/12/2004")
        db.session.add(c)
        db.session.commit()
        # db.create_all()