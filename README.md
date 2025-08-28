Finance Tracker CLI

A command-line tool for personal finance management. This application provides a simple and efficient way to track income and expenses, helping users stay on top of their financial goals.

The project is built on a robust backend using Python and SQLAlchemy ORM for database interactions, with Alembic handling all database migrations.

 Features

    Add Transactions: Easily log new income and expense entries.

    View Transactions: Quickly see a summary of your most recent transactions.

    Update & Delete: Modify or remove entries to keep your records accurate.

    Monthly Summary: Generate a detailed report of your total income, expenses, and net balance for any given month.

Get Started

Follow these steps to set up and run the application on your local machine.

Installation

    Clone the repository:
    Bash

git clone <your-repository-url>
cd finance_tracker

Install dependencies:
This project uses pipenv to manage dependencies. If you don't have it, you can install it with pip install pipenv.
Bash

pipenv install

Run database migrations:
This command will set up your database and create all the necessary tables.
Bash

    pipenv run alembic upgrade head

Usage

All commands are executed using pipenv run python -m bin.cli.

Add a Transaction

To add an entry, use the add command.

    Example (Expense):
    Bash

pipenv run python -m bin.cli add --amount 45.75 --type expense --category "Food" --desc "Lunch with a friend"

Example (Income):
Bash

    pipenv run python -m bin.cli add --amount 1500 --type income --category "Freelance" --desc "Consulting project payment"

View Recent Transactions

Use the view-recent command to see the 10 most recent transactions.
Bash

pipenv run python -m bin.cli view-recent

Update a Transaction

Use the transaction's ID to update its details. You can update one or more fields at a time.
Bash

# Update the amount and description for transaction ID 1
pipenv run python -m bin.cli update 1 --amount 50 --desc "Lunch with a friend, drinks included"

Delete a Transaction

To permanently remove a transaction, use the delete command with its ID.
Bash

pipenv run python -m bin.cli delete 1

Get a Monthly Summary

To see a breakdown of your finances for a specific month, use the summary command.
Bash

pipenv run python -m bin.cli summary --month 12 --year 2024

👤 Author

    Joe Kariuki

    GitHub: @Spiffy047

    Email: mwanikijoe1@gmail.com