def get():
    while True:
        user_input = input("Please enter an integer: ")
        try:
            return int(user_input)
        except ValueError:
            print("Error: That is not a valid integer. Please try again.")

number = get()
print(f"You entered the integer: {number}")