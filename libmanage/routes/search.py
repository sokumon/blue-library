from libmanage import app
from flask import request
from libmanage.handlers.search import search_and_paginate_books
@app.get("/search")
def search():
    search_term = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    books,has_next, has_prev = search_and_paginate_books(search_term, page, per_page)
    found_books = []
    for value in books:
        value.__dict__.pop('_sa_instance_state',None)
        temp = value.__dict__.copy()
        found_books.append(temp)
    status = {
        "books":found_books
    }
    status["has_next"] = has_next
    status["has_prev"] = has_prev
    return status