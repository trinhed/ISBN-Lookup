# ISBN-Lookup

The ISBN Lookup service utilizes isbn_service.py, isbn_request.py, request.txt, and response.txt. The isbn request prompts the user to enter an ISBN and write that ISBN to request.txt. the isbn service reads the request.txt file and makes a call to the Open Library API to retrieve book information. Once the book information is retrieved, the isbn service writes that information in JSON format to the response.txt file.
