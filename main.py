#LIBRARY BORROW SYSTEM
print("Library Borrow System")
print("**********************")
store_book = {}
import string
running = True
while running:
    user_input = input("'stop' to quit Enter to continue: ")
    if user_input.lower() == "stop":
        print("Goodbye 🙋‍♂️🙋‍♂️")
        break

    print("What would you like to do?")
    print("**************************")
    print("1. Store book")
    print("2. Borrow book")
    print("3. Return Books")
    print("4. show all Books")

    user_option = input("Enter your choice: ")
    if user_option == "1":
        title = input("Enter book title: ").capitalize()
        num_copies = int(input("How many copies would you like to add? "))
        store_book[title] = num_copies
        print(f"✅✅ you have stored: {title} having {num_copies} copies")
        print("**************************")

    if user_option == "2":
        title = input("Enter book title: ").capitalize()
        if title in store_book:
            Quantity = int(input("How many copies would you like to borrow? "))
            remaining  = store_book[title] - Quantity
            print(f"you have borrowed: {Quantity} copies,remaining copies is {remaining} ")
            print("**************************")
        else:
            print("❌❌ Sorry, no such book exists")

    if user_option == "3":
        title = input("Enter book title: ").capitalize()
        if title in store_book:
            Quantity1 = int(input("How many copies would you like to return? "))
            new_quantity = store_book[title] + Quantity1
            print(f"you have returned: {Quantity1} copies of {title} having {new_quantity} copies")
            print("**************************")

        else:
            print("❌❌ <UNK> Sorry, no such book exists")

    elif user_option == "4":
        if not store_book:
            print("<UNK> No book exists")
        else:
            print("All the books in the Library")
            print("*****************************")
            for title, num_copies in store_book.items():
                print(f"{title}: {num_copies} copies")