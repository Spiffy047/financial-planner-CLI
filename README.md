Finance Tracker CLI

This is a simple command-line tool for tracking personal finances. It lets you quickly log your income and expenses, review your recent transactions, and get a monthly summary of your spending.

The app is built in Python and uses SQLAlchemy ORM to manage a local database, with Alembic handling database migrations.

Features

    Add new transactions: Record an income or an expense with an amount, category, and description.

    View recent transactions: See the last 10 transactions you've logged.

    Generate monthly reports: Get a summary showing your total income, expenses, and net balance for any given month.

    Update existing transactions: Modify an existing transaction's details.

    Delete transactions: Remove a transaction from your records.

Setup

To get this running on your local machine, follow these steps:

    Clone the project:
    Bash

git clone <your-repository-url>
cd finance_tracker

Install dependencies:
This project uses pipenv. If you don't have it, install it first with pip install pipenv, then run:
Bash

pipenv install

Set up the database:
The database schema is managed with Alembic. Run the following command to create the necessary tables:
Bash

    pipenv run alembic upgrade head

How to Use

All commands are run with pipenv run python -m bin.cli. Here are a few examples:

Add a new transaction

    For an expense:
    Bash

pipenv run python -m bin.cli add --amount 55 --type expense --category "Groceries" --desc "Weekly food shopping"

For income:
Bash

    pipenv run python -m bin.cli add --amount 2500 --type income --category "Freelance" --desc "Project payment"

Check recent activity

    Simply run the view-recent command to see your latest 10 transactions and their IDs.
    Bash

    pipenv run python -m bin.cli view-recent

Update a transaction

    Use the transaction's ID to modify it. You only need to specify the fields you want to change.
    Bash

    pipenv run python -m bin.cli update 1 --amount 60 --desc "Weekly shopping plus drinks"

Delete a transaction

    Use the transaction's ID to permanently delete it from the database.
    Bash

    pipenv run python -m bin.cli delete 1

Get a monthly summary

    Specify the month and year to see your financial summary.
    Bash

    pipenv run python -m bin.cli summary --month 8 --year 2025

