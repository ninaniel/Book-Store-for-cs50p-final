<div style="text-align:center; color: rgb(106, 90, 205)"> <h1> Bookstore Application </h1> </div> 

----------

<h4 style="text-align:center; font-weight: bold;"> Welcome to the Bookstore Application! </h4>

This Python program is designed to manage a bookstore, allowing users to browse through various book collections, add books to their shopping cart, and generate invoices. The application is now built using object-oriented principles, featuring classes for books, collections, and invoices.

The application dynamically loads book data from a `collections.json` file, with support for different categories of books.

## Description and Features:

### Features:
- Browse through multiple book collections by category or century.
- View books in a paginated table format with title, author, and price.
- Add books to the shopping cart and manage quantities.
- Remove books from the cart and view updated cart details.
- Checkout, review cart, and generate a detailed PDF invoice.
- Exit the application gracefully after completing or canceling a transaction.

### Main Classes Descriptions:

#### `Book` class:
Represents a book with attributes like `index`, `title`, `author`, and `price`.

#### `Collection` class:
Stores a collection of books and supports pagination (viewing books in chunks, like pages).

#### `Invoice` class:
Manages the shopping cart by adding/removing books, displaying cart contents, and generating a PDF invoice.

#### `BookstoreApp` class:
Handles user interaction, displaying menus, navigating through books, adding books to the cart, and managing the entire book browsing and purchasing process.

### Key Features and Updates:
- **Category Selection**: Browse through books based on categories such as "Books You Must Read Before You Die", "Science Fiction & Fantasy", "History Books", and more.
- **Pagination**: Browse through books in paginated format, viewing 100 books at a time.
- **Shopping Cart**: Add and remove books, view the total price, and manage cart items with quantity.
- **Checkout**: At checkout, the program prompts for customer details (name, address) and generates a PDF invoice.
- **Invoice Generation**: Once the purchase is confirmed, a detailed invoice is generated as a PDF, displaying the books, prices, and customer details.

Example book display:
+-----+---------------------------------------------------------------------------------+-------------------------------------------+----------+   
|   N | 📝 Title                                                                        | 🤓 Author                                 | 💲Price  |
+=====+=================================================================================+===========================================+==========+   
|   1 | Hamlet                                                                          | William Shakespeare                       | 25.5$    |   
+-----+---------------------------------------------------------------------------------+-------------------------------------------+----------+   
|   2 | Macbeth                                                                         | William Shakespeare                       | 11.04$   |   
+-----+---------------------------------------------------------------------------------+-------------------------------------------+----------+
|   3 | Don Quixote                                                                     | Miguel de Cervantes Saavedra              | 14.38$   |
...
+-----+---------------------------------------------------------------------------------+-------------------------------------------+----------+
|  99 | The Leopard                                                                     | Giuseppe Tomasi di Lampedusa              | 17.62$   |
+-----+---------------------------------------------------------------------------------+-------------------------------------------+----------+
| 100 | Thérèse Raquin                                                                  | Émile Zola                                | 39.23$   |
+-----+---------------------------------------------------------------------------------+-------------------------------------------+----------+ 


**Shopping Cart Example**:
Users can review the item(s) added to the shopping bag.
📌 Items:
 -  --------------------
1  The Leopard - $17.62
2  Hamlet - $25.5
-  --------------------
📌 Total Price: $43.12


### Main Functions:

- **`load_collections()`**: Loads book collections from the `collections.json` file.
- **`load_books()`**: Displays books in a paginated table format based on the current collection and page.
- **`select_book()`**: Adds a selected book to the shopping cart and prompts the user for further actions (checkout, remove item, etc.).
- **`generate_pdf()`**: Generates an invoice PDF after a purchase, including customer information and purchased items.
- **`next_page()` / `previous_page()`**: Navigates between pages of books for browsing.
- **`validate_input()`**: Ensures that the user inputs valid numbers when selecting options.

### Running the Application:

## Installation and usage:
1. Clone the repository or download the source code files.
git clone https://github.com/ninaniel/


2. Install the required dependencies:
pip install -r requirements.txt


3. Run the project.py file to start the application:
python bookstore.py


4. Follow the on-screen prompts to browse books, add them to your cart, and proceed to checkout.

## Dependencies:

- `tabulate`: For creating formatted tables for displaying books.
- `FPDF`: For generating PDF invoices.
- `json`: For handling data from the `collections.json` file.
- `datetime`: For adding timestamp information to invoices.

### Example of Generated Invoice:
After completing a purchase, the application generates an invoice in PDF format, which includes details like customer name, address, a list of books purchased, their prices, and the total price.

<div style="text-align:center;"> <img src="./invoice.png" alt="invoice"> </div>

## Credits

This application was created by <span style="color: rgb(106, 90, 205); font-weight: bold; "> Bagsmen </span>