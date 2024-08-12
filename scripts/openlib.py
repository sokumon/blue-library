import requests

def fetch_books_by_genre(genre, limit=10):
    # Query the Open Library API for books in a specific genre
    url = f"https://openlibrary.org/subjects/{genre.lower()}.json?limit={limit}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        books = data.get('works', [])
        
        if books:
            for book in books:
                title = book.get('title', 'N/A')
                authors = ', '.join([author.get('name', 'N/A') for author in book.get('authors', [])])
                
                # Fetch more details about the book, including ISBN
                work_key = book.get('key')
                if work_key:
                    detail_url = f"https://openlibrary.org{work_key}.json"
                    detail_response = requests.get(detail_url)
                    if detail_response.status_code == 200:
                        detail_data = detail_response.json()
                        isbn_list = detail_data.get('isbn_10', []) + detail_data.get('isbn_13', [])
                        isbn_str = ', '.join(isbn_list)
                    else:
                        isbn_str = 'N/A'
                else:
                    isbn_str = 'N/A'
                
                print(f"Title: {title}")
                print(f"Author(s): {authors}")
                print(f"ISBN(s): {isbn_str}")
                print('-' * 40)
        else:
            print(f"No books found for the genre: {genre}")
    else:
        print(f"Failed to fetch data. HTTP Status code: {response.status_code}")

if __name__ == "__main__":
    genre = input("Enter the genre to search for: ")
    fetch_books_by_genre(genre)
