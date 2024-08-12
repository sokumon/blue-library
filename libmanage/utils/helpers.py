from libmanage import db
from libmanage.dbschema import Book,Member,Transaction
from datetime import datetime

# small function to in writing dues after each return
def calculate_due(book_id,member_id):
    previous_issue = Transaction.query.filter_by(
        book_id=book_id,
        member_id=member_id,
        transaction_type='Issue'
    ).order_by(Transaction.date.desc()).first()
    
    if previous_issue:
        current_date = datetime.now()
        print(previous_issue.date)
        due_date = datetime.strptime(previous_issue.date, '%d/%m/%Y')
        if current_date > due_date:
            overdue_days = (current_date - due_date).days


            due_amount = overdue_days * 10

            member = Member.query.get(member_id)
            if member:
                member.due += due_amount
                db.session.commit()
                print(f"Updated dues for Member ID {member_id}. New due amount: {member.due}")
                change_memebership(member_id)
                return True
            else:
                print(f"Member with ID {member_id} not found.")
        else:
            print("No overdue days to calculate.")
    else:
        print(f"No previous issues found for Book ID {book_id} and Member ID {member_id}.")
        return False
    



# small function to update Active or NA on each read of Members
def change_memebership(member_id):

    member = Member.query.get(member_id)
    
    if member:
        if member.due > 300:
            member.status = "NA"
        else:
            member.status = "Active"

        db.session.commit()
        print(f"Member ID {member_id} status updated to {member.status}.")
    else:
        print(f"Member with ID {member_id} not found.")


# a small function to update the quantity after each issue
def change_quantity(mode, book_id):
    book = Book.query.get(book_id)
    if book:
        if mode == "decrement":
            if book.quantity > 0:
                book.quantity -= 1
            else:
                print("Quantity is already at 0, cannot decrement.")
                return
        elif mode == "increment":
            book.quantity += 1
        else:
            print("Invalid mode. Use 'decrement' or 'increment'.")
            return
        
        # Commit the changes to the database
        db.session.commit()
        print(f"Updated quantity for Book ID {book_id}. New quantity: {book.quantity}")
    else:
        print(f"Book with ID {book_id} not found.")
        

