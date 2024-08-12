import requests
import json
def get_author(work_response):
    for author in work_response.get("authors", []):
        author_url = f"{base_url}{author['author']['key']}.json"
        author_res = requests.get(author_url)
        author_res_json = author_res.json()
        return author_res_json.get("name", "Unknown Author")
    return "Unknown Author"

def get_title(work):
    title = work.get("title", "Unknown Title")
    return title

def get_isbn(work_response_json):   
    if 'entries' in work_response_json and len(work_response_json['entries']) > 0:
        first_entry = work_response_json['entries'][0]
        isbn_10 = first_entry.get('isbn_10')
        isbn_13 = first_entry.get('isbn_13')
        if isbn_10:
            return isbn_10
        elif isbn_13:
            return isbn_13
    print(f"No ISBN found in entry for work: {work['key']}")
    return None

genres = ["programming", "architecture", "history"]
base_url = "https://openlibrary.org"

for genre in genres:
    url = f"{base_url}/subjects/{genre}.json"
    print(url)
    response = requests.get(url)
    subject_data = response.json()
    for work in subject_data.get("works", []):

        if "works" not in subject_data or len(subject_data["works"]) == 0:
            print(f"No works found for genre: {genre}")
            continue

        work_url = f"{base_url}{work['key']}/editions.json"
        work_response = requests.get(work_url)
        work_response_json = work_response.json()



        title = get_title(work_response_json)
        author = get_author(work_response_json)
        isbn = get_isbn(work_response_json)

        # Ensure payload contains the data obtained
        payload = {
            "name": title,
            "author": author,
            "isbn": isbn[0] if isbn else "Unknown ISBN",
            "genre": genre.capitalize(),
            "quantity":3 # Capitalize genre for better readability
        }

    print(payload)
    # # POST request URL
    # post_url = "http://127.0.0.1:5000/create/books"
    
    # # Make the POST request with the payload
    # response = requests.post(post_url, json=payload)

    # # Print response from the server
    # print(response.json())