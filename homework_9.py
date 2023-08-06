ADDRESSBOOK = {}

def add_handler(data):
    name, phone = data
    name = name.title()
    ADDRESSBOOK[name] = phone
    return f"The contact {name}: {phone} is added"

def change_handler(data):
    name, phone = data
    name = name.title()
    if name not in ADDRESSBOOK:
        raise KeyError(f"The contact {name} is not found")
    ADDRESSBOOK[name] = phone
    return f"The number for {name} is changed {phone}"

def phone_handler(data):
    name = data[0].title()
    phone = ADDRESSBOOK.get(name)
    if phone is None:
        raise KeyError(f"The contact {name} is not found")
    return f"The number for {name}: {phone}"

def show_all_handler(*args):
    if not ADDRESSBOOK:
        return "Empty list"
    contacts = "\n".join(f"{name}: {phone}" for name, phone in ADDRESSBOOK.items())
    return "The list of contacts:\n" + contacts

def exit_handler(*args):
    return "Good bye!"

def hello_handler(*args):
    return "How can I help you?"

def command_parser(raw_str: str):
    elements = raw_str.split(maxsplit=1)
    command = elements[0].lower()

    if command in COMMANDS:
        data = elements[1].split()
        return COMMANDS[command], data
    else:
        raise ValueError("Please enter valid command.")

def input_error(wrap):
    def inner():
        try:
            result = wrap()
            return result
        except IndexError:
            return "Give me name and phone please."
        except ValueError:
            return "Please enter valid command."
        except KeyError:
            return "Please enter the name and phone."

    return inner

COMMANDS = {
    "hello": hello_handler,
    "add": add_handler,
    "change": change_handler,
    "phone": phone_handler,
    "show": show_all_handler,
    "good": exit_handler,
    "bye": exit_handler,
    "close": exit_handler,
    "exit": exit_handler,
}

@input_error
def main():
    while True:
        user_input = input(">>> ")
        if not user_input:
            continue
        if user_input == 'hello':
            print(hello_handler())
            continue

        func, data = command_parser(user_input)
        result = func(data)
        print(result)
 
        if func == exit_handler:
            break

if __name__ == "__main__":
    main()
