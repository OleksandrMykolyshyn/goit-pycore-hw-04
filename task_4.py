def parse_input(user_input):
    parts = user_input.strip().lower().split()
    cmd = parts[0] if parts else ""
    args = parts[1:]
    return cmd, args

def hello_handler():
    return "How can I help you?"

def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage: add <username> <phone>"
    username, phone = args
    contacts[username] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Usage: change <username> <phone>"
    username, phone = args
    if username in contacts:
        contacts[username] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def get_phone(args, contacts):
    if len(args) != 1:
        return "Usage: phone <username>"
    username = args[0]
    return contacts.get(username, "Contact not found.")

def get_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(hello_handler())
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()