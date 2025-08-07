# ISBN-Lookup

The ISBN Lookup service utilizes isbn_service.py, isbn_request.py, request.txt, and response.txt. The isbn request prompts the user to enter an ISBN and write that ISBN to request.txt. the isbn service reads the request.txt file and makes a call to the Open Library API to retrieve book information. Once the book information is retrieved, the isbn service writes that information in JSON format to the response.txt file.


# Request:
<img width="857" height="119" alt="Screenshot 2025-08-07 at 12 04 11 AM" src="https://github.com/user-attachments/assets/72664097-714f-4220-9169-c1e3e6f4e711" />

# Response:
{"isbn": "9780201616224", "title": "The Pragmatic Programmer", "author": "Andy Hunt & David Thomas & Dave Thomas & Andrew Hunt & David . Thomas", "publisher": "Addison-Wesley", "publish_date": "2000"}
