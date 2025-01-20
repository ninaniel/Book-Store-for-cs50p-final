import sys
import json
from tabulate import tabulate
import random
from fpdf import FPDF
from datetime import datetime

class Book:
    def __init__(self, index, title, author, price):
        self.index = index
        self.title = title
        self.author = author
        self.price = price

class Collection:
    def __init__(self, books):
        self.books = books

    def get_books_paginated(self, start_row, end_row):
        return self.books[start_row - 1:end_row - 1]

class BookstoreApp:
    def __init__(self):
        self.start_row = 1
        self.end_row = 101
        self.page = 1
        self.collections = self.load_collections()
        self.invoice = Invoice()

    def load_collections(self): # load collections from json
        try:
            with open("collections.json", "r") as file:
                data = json.load(file)
                collections = {}
                for key, books in data.items():
                    collections[key] = Collection([Book(**book) for book in books])
                return collections
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error: Unable to load collections from collections.json.")
            sys.exit(1)

    def run(self):
        self.greeting()

        while True:
            self.display_main_menu()
            user_choice = self.validate_input(1, 7)
            collection_key = f"collection_{user_choice}"

            if user_choice == 7:
                self.exit()
            
            elif user_choice == 6:
                while True:
                    try:
                        user_input = int(input("Please, enter the century (17/18/19/20/21): "))
                        if 17 <= user_input <= 21:
                            collection_key = f"collection_{user_input}"
                            break
                    except ValueError:
                        pass   


            while True:
                books = self.load_books(collection_key)
                self.display_shopping_menu()

                shopping_choice = self.get_choice(["a", "b", "c", "d", "e"])

                if shopping_choice == "a":
                    self.select_book(books)
                elif shopping_choice == "b":
                    self.next_page()
                elif shopping_choice == "c":
                    self.previous_page()
                elif shopping_choice == "d":
                    break
                elif shopping_choice == "e":
                    self.exit()

    def validate_input(self, start, end):
        while True:
            try:
                user_input = int(input("➡ Your choice: "))
                if start <= user_input <= end:
                    return user_input
                print("Invalid choice. Please enter a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_choice(self, valid_choices):
        while True:
            choice = input("➡ Enter your choice: ").lower()
            if choice in valid_choices:
                return choice
            print("Invalid choice. Please enter a valid option.")

    def load_books(self, collection_key):
        collection = self.collections.get(collection_key)
        if not collection:
            print("Invalid collection key.")
            return []

        paginated_books = collection.get_books_paginated(self.start_row, self.end_row)
        headers = ["N", "📝 Title", "🤓 Author", "💲Price"]
        table_data = [[book.index, book.title, book.author, f'{book.price}$'] for book in paginated_books]

        if table_data:
            print(tabulate(table_data, headers=headers, tablefmt="grid", maxcolwidths=[None, 70, None, None]))
            print(f"\n📌 Page - {self.page} / {len(collection.books) // 100 + (1 if len(collection.books) % 100 else 0)}")
        else:
            print("No books found on this page.")

        return paginated_books

    def select_book(self, books):
        while True:
            try:
                book_choice = int(input("Enter the number of the book you want to buy: "))
                selected_book = next((book for book in books if book.index == book_choice), None)
                self.invoice.add_item(selected_book)               
                break
            except (ValueError, AttributeError):
                print("⚠ Please, enter a valid book number.")

        print(f"\nYou have added: 📖 {selected_book.title} - ${selected_book.price}")

        while True:
            self.checkout_menu()
            checkout_choice = self.get_choice(["1", "2", "3", "4", "5"])

            match checkout_choice:
                case "1":
                    self.invoice.display_items()
                    self.checkout()
                    return
                case "2":
                    return
                case "3":
                    self.invoice.display_items()
                    while True:
                        try:
                            item_to_remove = int(input("\nEnter the book number to remove: "))
                            self.invoice.remove_item(item_to_remove)
                            
                            if not self.invoice.items:
                                self.empty_bag_options(prompt="Your shopping bag is now empty.")
                                return
                            
                            break
                        except (ValueError, IndexError):
                            print("⚠ Please, enter a valid book number to remove.")
                case "4":
                    self.invoice.display_items()
                    input("Press any key to go back.")
                case "5":
                    self.empty_bag_options(prompt="Shopping bag cleared. Returning to the main menu.")
                    return
                case _:
                    print("Invalid choice. Please enter a valid option.")

    def checkout(self):
        while True:
            pay_choice = input(f"\n📌 Total Price: ${self.invoice.total_price}\n\nConfirm payment? (yes/no): ").lower()                           
            match pay_choice:
                case 'yes':
                    self.invoice.generate_pdf()
                    self.exit(message="Invoice created ✔. Thank you for purchase!")
                case "no":
                    self.empty_bag_options(prompt="Payment canceled. Shopping bag is empty.")
                    return 
                case _:
                    continue  

    def empty_bag_options(self, prompt="Shopping bag is empty."):
        self.invoice.items.clear()
        self.invoice.total_price = 0

        while True:
            choice = input(f"{prompt}\n🛒 Continue shopping? (yes/no): ").lower()
            
            if choice == 'yes':           
                return
            elif choice == 'no':
                self.exit()
            else:
                continue

    def next_page(self):
        if self.page < 3:
            self.start_row += 100
            self.end_row += 100
            self.page += 1

    def previous_page(self):
        if self.page > 1:
            self.start_row -= 100
            self.end_row -= 100
            self.page -= 1

        
    def greeting(self):
        print("📚 Welcome to our Book Shop 📚",
              "\n🧐 Searching for some good books to enjoy yourself?",
              "⬇ Have a look at our collections! ⬇", sep="\n")

    def display_main_menu(self):
        print("\n➡ Choose a category:",
              "1. Books You Must Read Before You Die",
              "2. Science Fiction & Fantasy Books",
              "3. History Books",
              "4. Memoir / Biography / Autobiography",
              "5. Motivational and Self-Improvement Books",
              "6. Best Books by Century",
              "7. ❌ Exit", sep="\n")

    def display_shopping_menu(self):
        print("\n⚠ Actions:\n",
              "a) 📕 Choose a book to buy",
              "b) 📜 Next page",
              "c) 📜 Previous page",
              "d) 📚 Go Back to Main Collections",
              "e) ❌ Exit", sep="\n")
        
    def checkout_menu(self):
        print("\n⚠ Items in the shopping bag:",
              f"{len(self.invoice.items)}",
              f"⚠ Total Price: ${self.invoice.total_price}",
              "\n1. ✅ Check-out",
              "2. ➕ Add item",
              "3. ➖ Remove item",
              "4. 🛒 Display shopping bag",
              "5. ❌ Cancel", sep="\n")

    def exit(self, message = "Thank you for visiting! \nExiting.."):
        sys.exit(message)

class Invoice:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_item(self, book):
        self.items.append(f"{book.title} - ${book.price}")
        self.total_price = round(self.total_price + book.price, 2)


    def remove_item(self, index):
        try:
            removed_item = self.items.pop(index - 1)
            price = float(removed_item.split("$")[-1])
            self.total_price = round(self.total_price - price, 2)
            print(f"Removed: {removed_item}")
        except IndexError:
            print("⚠ Please, enter a valid book number to remove.")
            return


    def generate_pdf(self):
        if not self.items:
            print("No items in your cart. Thank you for visiting!")
            return

        # Asking user for customer info
        while True:
            name = input("⚠ Please, enter your personal information for Invoice\nYour name: ").title()
            address = input("Your address: ").capitalize()
            if name and address:
                break

        # Create PDF
        pdf = FPDF()
        pdf.add_page()

        # Title
        pdf.set_font("Arial", "B", 24)
        pdf.cell(0, 20, "INVOICE", ln=True, align="C")

        # Store name
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Book Store", ln=True, align="C")

        # Invoice and order info
        pdf.ln(10)
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, f"Invoice #: {str(random.randint(100000, 999999))}", ln=False, align="L")
        pdf.cell(0, 10, f"Order #: {str(random.randint(100000, 999999))}", ln=True, align="R")
        
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M')
        pdf.cell(0, 10, f"Invoice Date: {current_datetime}", ln=False, align="L")
        pdf.cell(0, 10, f"Order Date: {current_datetime}", ln=True, align="R")

        # Customer info
        pdf.ln(10)
        pdf.cell(0, 7, "Invoice To", ln=True)
        pdf.cell(0, 7, f"Customer Name: {name}", ln=True)
        pdf.cell(0, 7, f"Address: {address}", ln=True)

        # Product table headers
        pdf.ln(10)
        pdf.set_font("Arial", "B", 12)
        pdf.set_fill_color(0, 128, 0)  # Green background
        page_width = pdf.w - (pdf.l_margin + pdf.r_margin)
        pdf.cell(0.75 * page_width, 10, "Product Description", 1, 0, "C", fill=True)
        pdf.cell(0.25 * page_width, 10, "Unit Price", 1, 1, "C", fill=True)

        # Product details
        pdf.set_font("Arial", "", 12)
        for item in self.items:
            description, price = item.split(" - ")
            pdf.cell(0.75 * page_width, 10, description, 1, 0, "L")
            pdf.cell(0.25 * page_width, 10, price, 1, 1, "R")

        # Total price
        pdf.ln(10)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, f"Total Price: ${self.total_price}", ln=True, align="R")

        # Save PDF
        pdf.output("invoice.pdf")
        print(f"\n✅ Invoice generated: invoice.pdf")


    def display_items(self):
        if not self.items:
            print("Your shopping bag is empty.")
        else:
            print("\n🛒 Shopping Bag:")
            for i, item in enumerate(self.items, 1):
                print(f"{i}. {item}")

if __name__ == "__main__":
    app = BookstoreApp()
    app.run()
