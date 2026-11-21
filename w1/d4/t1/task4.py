# List of usernames
usernames = ["ikra", "riya123", "aman", "krishna", "john12", "sam"]

# Filter usernames having at least 6 characters
filtered_usernames = list(filter(lambda name: len(name) >= 6, usernames))

# Print the result
print("Original Usernames:", usernames)
print("Filtered Usernames:", filtered_usernames)