from libmanage import db

class User(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)

class Book(db.Model):
    id = db.Column(db.String(100),primary_key=True)
    name = db.Column(db.String(1000),nullable=False)
    author = db.Column(db.String(500),nullable=False)
    isbn = db.Column(db.BigInteger,nullable=False)
    genre = db.Column(db.String(20), nullable=True)
    quantity = db.Column(db.Integer,nullable=False)

class Member(db.Model):
    id = db.Column(db.String(100),primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    phoneno = db.Column(db.BigInteger,nullable=True)
    active = db.Column(db.String(5), nullable=False)
    due = db.Column(db.Integer, nullable=True)

class Transaction(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    book_id = db.Column(
        db.String(100), 
        db.ForeignKey('book.id', ondelete='CASCADE'), 
        nullable=False
    )
    member_id = db.Column(
        db.String(100),
        db.ForeignKey('member.id', ondelete='CASCADE'),
        nullable=False
    )
    date = db.Column(db.String(20), nullable=False)
    transaction_type = db.Column(db.String(10), nullable=False)
