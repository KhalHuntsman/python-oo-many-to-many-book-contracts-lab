#!/usr/bin/env python3

# Author: Hunter Steele
# Date: 12/8/25
# Version 1.1

class Author:
    # Class-level list that stores every Author instance
    all = []

    def __init__(self, name):
        self.name = name                     # Simple attribute, no validation required
        Author.all.append(self)              # Track every Author created

    def contracts(self):
        # Return all Contract objects where this Author is the author
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # Use Contract as intermediary to return all Books this Author has contracts for
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        # Create and return a new Contract instance associated with this Author
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Sum royalties from all contracts belonging to this Author
        return sum(contract.royalties for contract in self.contracts())


class Book:
    # Class-level list to store all Book instances
    all = []

    def __init__(self, title):
        self.title = title                   # Simple string attribute
        Book.all.append(self)                # Track every Book created

    def contracts(self):
        # Return all Contract objects where this Book is the book
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # Use Contract as intermediary to return all Authors associated with this Book
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    # Class-level list to keep track of every Contract instance
    all = []

    def __init__(self, author, book, date, royalties):
        # Each attribute assignment triggers property validation below
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)            # Store the newly created Contract

    # --- Author Validation ---
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        # Must be an Author instance
        if not isinstance(value, Author):
            raise TypeError("author must be an instance of Author.")
        self._author = value

    # --- Book Validation ---
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        # Must be a Book instance
        if not isinstance(value, Book):
            raise TypeError("book must be an instance of Book.")
        self._book = value

    # --- Date Validation ---
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        # Must be a string representing a date
        if not isinstance(value, str):
            raise TypeError("date must be a string.")
        self._date = value

    # --- Royalty Validation ---
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        # Must be an integer
        if not isinstance(value, int):
            raise TypeError("royalties must be an integer.")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        # Return all Contract objects matching the given date string
        return [contract for contract in cls.all if contract.date == date]
