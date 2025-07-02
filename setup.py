def menu(options: list[str], prompt: str, header: str) -> str:
    print(header)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    while True:
        try:
            c = int(input(f"{prompt} > "))
            if 1 <= c <= len(options):
                return options[c - 1]
            else:
                print(f"Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return None
