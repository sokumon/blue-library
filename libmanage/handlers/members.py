from libmanage import db
from libmanage.dbschema import Member

def create_member(id,name,phoneno,active,due):
    member =  Member(id=id,name=name,phoneno=phoneno,active=active,due=due)
    db.session.add(member)
    db.session.commit()
    return True

def update_member(id,changes):
    member = Member.query.filter_by(id=id).first()
    for key, value in changes.items():
        setattr(member, key, value)
    db.session.commit()

def delete_member(id):
    Member.query.filter_by(id=id).delete()
    db.session.commit()

def read_all_members():
    return Member.query.all()