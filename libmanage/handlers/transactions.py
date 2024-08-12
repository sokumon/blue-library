from libmanage import db
from libmanage.dbschema import Transaction,Member,Book
from libmanage.utils.helpers import calculate_due,change_quantity

def create_transaction(id,book_id,member_id,transaction_type,date_time=None):
    book = Book.query.get(book_id)
    member = Member.query.get(member_id)
    if transaction_type == "Return":
        if calculate_due(book_id,member_id):
            transact =  Transaction(id=id,book_id=book.id,member_id=member.id,date=date_time,transaction_type=transaction_type)
            db.session.add(transact)
            db.session.commit()
            change_quantity("increment", book_id)
            return True
        else:
            return False
    else:
        transact =  Transaction(id=id,book_id=book.id,member_id=member.id,date=date_time,transaction_type=transaction_type)
        db.session.add(transact)
        db.session.commit()
        change_quantity("decrement", book_id)
        return True 

def update_transaction(id,changes):
    transact = Transaction.query.filter_by(id=id).first()
    for key, value in changes.items():
        setattr(transact, key, value)
    db.session.commit()

def delete_transaction(id):
    Transaction.query.filter_by(id=id).delete()
    db.session.commit()

def read_all_transactions():
    transactions = (
        db.session.query(Transaction, Book.name, Member.name)
        .join(Book, Transaction.book_id == Book.id)
        .join(Member, Transaction.member_id == Member.id)
        .all()
    )
    
    results = []
    
    for transaction, book_name, member_name in transactions:
        transaction_dict = transaction.__dict__.copy()
        transaction_dict.pop('_sa_instance_state', None)
        transaction_dict['book_name'] = book_name
        transaction_dict['member_name'] = member_name
        results.append(transaction_dict)
    return results