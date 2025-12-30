# Creating a decorator to check if user is logged in
def login_required(func):

    # Wrapper function
    def wrapper():
        print("Checking login status...")

        # Extra behavior before calling original function
        remember_me = False   # assume user is logged in

        if remember_me:
            func()
        else:
            print("Access denied!")

    return wrapper


# Applying decorator to a function
@login_required
def dashboard():
    print("Welcome to your dashboard!")


# Calling the decorated function
dashboard()
