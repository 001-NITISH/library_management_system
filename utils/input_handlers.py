def get_validated_input(prompt, expected_type, allowed_values=None):
    while True:
        try:
            user_input = expected_type(input(prompt))
            if allowed_values and user_input not in allowed_values:
                raise ValueError
            return user_input
        except ValueError:
            print(f"Invalid input. Please enter a valid {expected_type.__name__}.")
