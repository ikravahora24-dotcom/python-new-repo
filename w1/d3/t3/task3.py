
# Create a nested dictionary representing a library
library = {
    101: {
        "title": "Python Programming",
        "author": "John Smith",
        "available_copies": 5
    },
    102: {
        "title": "Java Programming",
        "author": "James Gosling",
        "available_copies": 3
    },
    103: {
        "title": "Data Science",
        "author": "Mark Taylor",
        "available_copies": 4
    }
}

# Book ID to be issued
book_id = 102

# Display copies before issuing
print("Before issuing:")
print("Available copies:", library[book_id]["available_copies"])

# Check availability and issue the book
if library[book_id]["available_copies"] > 0:
    library[book_id]["available_copies"] -= 1
    print("Book issued successfully!")
else:
    print("Sorry! Book is not available.")

# Display copies after issuing
print("After issuing:")
print("Available copies:", library[book_id]["available_copies"])

# Display complete library
print("Library Records:", library)