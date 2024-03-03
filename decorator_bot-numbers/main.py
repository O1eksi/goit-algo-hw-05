contacts = {}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "You did not enter the phone number or forgot to put a space after the name. Please repeat the operation."
        except KeyError:
            return "This name is not entered in the phone book."
    return wrapper

@handle_errors
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@handle_errors
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

@handle_errors
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

def show_all():
    return contacts

def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()
        command, *args =  parse_input(command)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all())

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
