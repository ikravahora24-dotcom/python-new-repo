# Outer function
def make_greeting(language):

    # Inner function
    def greeting(name):

        if language == "english":
            print("Hello,", name)

        elif language == "hindi":
            print("Namaste,", name)

        else:
            print("Language not supported!")

    # Return inner function
    return greeting


# Create greeting functions
english_greeting = make_greeting("english")
hindi_greeting = make_greeting("hindi")

# Calling the returned functions
english_greeting("Ikra")
hindi_greeting("Ikra")