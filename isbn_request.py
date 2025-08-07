import os
import time

isbn = input("Enter ISBN: ")

with open("request.txt", "r+") as isbn_request: # Open request.txt to write ISBN to
    isbn_request.seek(0) # Move file cursor to top of file
    isbn_request.truncate(0) # Clear data in file
    isbn_request.write(isbn)
    time.sleep(3)
isbn_request.close()
