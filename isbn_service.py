import time
import requests
import json
import os

directory = "."

while True:
    time.sleep(1)
    # Check if requests.txt exists
    if not os.path.exists(os.path.join(directory, "request.txt")):
        raise FileNotFoundError

    # Get ISBN from request.txt
    with open("request.txt", "r") as request_file:
        isbn = request_file.read().strip()

    # Check if isbn exists
    if isbn:
        # Call Open Library API
        url = "https://openlibrary.org/api/books"
        params = {
            "bibkeys": f"ISBN:{isbn}",
            "format": "json",
            "jscmd": "data"
        }
        response = requests.get(url, params=params)
        isbn_info = response.json()
        book_isbn = f"ISBN:{isbn}"
        result = {}

        # Check if book exists in Open Library
        if book_isbn in isbn_info:
            book = isbn_info[book_isbn]

            result["isbn"] = isbn

            # Add book title if found
            if "title" in book: 
                result["title"] = book["title"]
            else:
                result["title"] = ""

            # Add author if found
            authors = []
            if "authors" in book:
                for author in book["authors"]:
                    if "name" in author:
                        authors.append(author["name"])
            if len(authors) > 0: # Check if there are multiple authors and join if yes
                result["author"] = " & ".join(authors)
            else:
                result["author"] = ""

            # Add publisher if found
            if "publishers" in book:
                publishers = book["publishers"]
                if len(publishers) > 0 and "name" in publishers[0]: # Check if there is a publisher name and store if yes
                    result["publisher"] = publishers[0]["name"]
                else:
                    result["publisher"] = ""
            else:
                result["publisher"] = ""

            # Add published date if found
            if "publish_date" in book:
                result["publish_date"] = book["publish_date"]
            else:
                result["publish_date"] = ""
        else: # Book doesn't exist in Open Library
            result = {}
            result["error"] = "Book not found"
            result["isbn"] = isbn

        # Write ISBN information to response.txt
        with open("response.txt", "w+") as response_file:
            response_file.write(json.dumps(result))
        response_file.close()
    request_file.close()