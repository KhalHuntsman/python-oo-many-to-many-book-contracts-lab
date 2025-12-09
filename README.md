# Book–Author–Contract System

A Python object-oriented model demonstrating many-to-many relationships using three core classes: Author, Book, and Contract.
This system is designed to show how objects can relate to one another through an intermediary class while enforcing data validation through properties.

## Overview

This project models a publishing environment where:

- Authors can sign multiple contracts for different books.
- Books can have multiple authors associated with them through those contracts.
- Contracts serve as the linking object, storing information such as contract date and royalties.
- The system uses class-level tracking, property validation, and intermediary lookup methods to demonstrate common OO patterns used in Python.

## Class Structure
### 1. Author

Represents a writer who may have one or more contracts with various books.

#### Key Features:

- Tracks all Author instances via Author.all
- Looks up related contracts and books via helper methods
- Can sign new contracts
- Computes total royalties earned

#### Methods
|Method |	Purpose |
|:------|:--------|
|contracts()|	Returns all Contract instances belonging to this author.
|books()|	Returns all Book instances associated with this author through contracts.
|sign_contract(book, date, royalties)|	Creates and returns a new Contract with this author.
|total_royalties()|	Sums all royalties across the author's contracts.

### 2. Book

Represents a published work that may have multiple contracts with different authors.

#### Key Features

- Tracks all Book instances via Book.all
- Can look up authors associated through Contract objects
- Mirrors the Author class’s relationship methods

#### Methods
|Method |	Purpose |
|:------|:--------|
|contracts()|	Returns all Contract instances associated with this book.
|authors()|	Returns all Author instances linked to this book through contracts.

### 3. Contract

The intermediary object linking Authors and Books.
Each Contract stores metadata such as date and royalties and enforces strict validation.

#### Key Features

- Tracks all Contract instances via Contract.all
- Enforces data integrity using property setters
- Provides class-level lookup by date

#### Properties (Validated)
|Property	|Type| Required	Validation|
|:--------|:--:|:-------------------|
|author	  |Author| instance	Raises TypeError if not an Author
|book	    |Book |instance	Raises TypeError if not a Book
|date     |str	|Must be a string
|royalties|int|	Must be an integer

Methods
|Method |	Purpose |
|:------|:--------|
|contracts_by_date(date) (class method)	| Returns all Contracts matching a given date string.


## Core Concepts Demonstrated
✔ Many-to-Many Relationships

Authors ↔ Contracts ↔ Books, with the Contract class acting as the intermediary.

✔ Class Attributes for Global Tracking

Each class maintains an .all list storing all instances for lookup.

✔ Data Validation Using Properties

Contract attributes enforce correct types, preventing invalid relationships or data.

✔ Helper Methods for Relationship Navigation

Methods like books(), authors(), and total_royalties() allow intuitive interaction with related data.

📌 Summary

This project provides a clear demonstration of:

Object composition

Many-to-many modeling in Python

Class-level tracking

Property-based validation

Relationship lookup methods

It serves as a solid architecture example for systems involving linked object sets such as publishing, inventory, employee/project matching, or student/course enrollment.