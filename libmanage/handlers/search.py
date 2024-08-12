from sqlalchemy import or_
from libmanage.dbschema import Book
def search_and_paginate_books(search_term, page, per_page):
    search = f"%{search_term}%"
    query = Book.query.filter(
        or_(
            Book.name.like(search),
            Book.author.like(search)
        )
    )
    users = query.paginate(page=page, per_page=per_page, error_out=False)
    return users.items, users.has_next, users.has_prev