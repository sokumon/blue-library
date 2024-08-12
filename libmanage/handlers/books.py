from libmanage import db
from libmanage.dbschema import Book
def create_book(id,name,author,isbn,genre,quantity):
    book =  Book(id=id,name=name,author=author,isbn=isbn,genre=genre,quantity=quantity)
    db.session.add(book)
    db.session.commit()
    return True

def update_book(id,changes):
    book = Book.query.filter_by(id=id).first()
    for key, value in changes.items():
        setattr(book, key, value)
    db.session.commit()

def delete_book(id):
    Book.query.filter_by(id=id).delete()
    db.session.commit()

def read_all_books():
    return Book.query.all()
    
