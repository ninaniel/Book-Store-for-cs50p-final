

import pytest
from project import load_books, buy_book, remove_item, next_page, previous_page, empty_bag_options



def test_load_books():
    books_list = load_books(1, 101, 1, 1)

    assert isinstance(books_list, list)
    assert len(books_list) == 100

def test_buy_book(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    books = [[1, "Book 1", "Author 1", "10.28$"],[2, "Book 2", "Author 2", "20.28$"]]
    checkout_items = []
    total_price = 0.0

    assert buy_book(books, checkout_items, total_price) == (["Book 1 - $10.28"], 10.28)

    monkeypatch.setattr('builtins.input', lambda _: "200")
    with pytest.raises(ValueError):
        buy_book(books, checkout_items, total_price)


def test_remove_item(monkeypatch):
    checkout_items = ['Book Title - $10.00', 'Book Title 2 - $20.00']
    monkeypatch.setattr('builtins.input', lambda _: '1')
    
    assert remove_item(checkout_items, 30.00) == (['Book Title 2 - $20.00'], 20.00)
    assert remove_item(checkout_items, 20.00) == ([], 0.00)


def test_next_page():
    start_row, end_row, page = next_page(1, 101, 1)
    assert start_row == 101
    assert end_row == 201
    assert page == 2
    assert next_page(101, 201, 2) == (201, 301, 3)
    assert next_page(201, 301, 3) == (201, 301, 3)

def test_previous_page():
    start_row, end_row, page = previous_page(201, 301, 3)
    assert start_row == 101
    assert end_row == 201
    assert page == 2
    assert previous_page(101, 201, 2) == (1, 101, 1)
    assert previous_page(1, 101, 1) == (1, 101, 1)


def test_empty_bag_options(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "no")
    with pytest.raises(SystemExit):
        empty_bag_options()