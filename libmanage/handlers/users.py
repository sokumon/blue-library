from libmanage import db
from libmanage.dbschema import User
def create_user(id,username,password):
    user =  User(id=id,username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return True
    
def update_user(id,changes):
    user = User.query.filter_by(id=id).first()
    for key, value in changes.items():
        setattr(user, key, value)
    db.session.commit()

def delete_user(id):
    User.query.filter_by(id=id).delete()
    db.session.commit()

def read_all_users():
    return User.query.all()
    
