
from sqlalchemy import func
from .models import Transaction, Category
from .database import Session
from datetime import datetime
import click

# Helper function to convert a Transaction object to a dictionary.
def _transaction_to_dict(transaction):
    """Converts a Transaction object to a dictionary."""
    return {
        "id": transaction.id,
        "amount": transaction.amount,
        "type": transaction.type,
        "category": transaction.category.name,
        "date": transaction.date.strftime("%Y-%m-%d"),
        "description": transaction.description
    }

def add_transaction(amount, type, category_name, desc):
    """Creates a new transaction in the database."""
    session = Session()
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)
        session.commit()
    
    new_transaction = Transaction(
        amount=amount,
        type=type,
        category=category,
        description=desc,
        date=datetime.now()
    )
    session.add(new_transaction)
    session.commit()
    session.close()

def get_transactions_as_list(limit=10):
    """Reads the most recent transactions from the database."""
    session = Session()
    transactions = session.query(Transaction).order_by(Transaction.date.desc()).limit(limit).all()

    transaction_dicts = [_transaction_to_dict(t) for t in transactions]
    
    session.close()
    
    return transaction_dicts

def get_monthly_summary(month, year):
    """Reads and aggregates transaction data for a specific month."""
    session = Session()
    
    total_income = session.query(func.sum(Transaction.amount)).filter(
        func.strftime('%Y-%m', Transaction.date) == f"{year}-{month:02}",
        Transaction.type == 'income'
    ).scalar() or 0
    
    total_expenses = session.query(func.sum(Transaction.amount)).filter(
        func.strftime('%Y-%m', Transaction.date) == f"{year}-{month:02}",
        Transaction.type == 'expense'
    ).scalar() or 0
    
    net_balance = total_income - total_expenses
    
    session.close()
    return (total_income, total_expenses, net_balance)

def update_transaction(transaction_id, new_amount, new_type, new_category_name, new_desc):
    """Updates an existing transaction by its ID."""
    session = Session()
    transaction = session.query(Transaction).filter_by(id=transaction_id).first()
    
    if not transaction:
        session.close()
        return False
    
    if new_amount:
        transaction.amount = new_amount
    if new_type:
        transaction.type = new_type
    if new_category_name:
        category = session.query(Category).filter_by(name=new_category_name).first()
        if not category:
            category = Category(name=new_category_name)
            session.add(category)
            session.commit()
        transaction.category = category
    if new_desc:
        transaction.description = new_desc

    session.commit()
    session.close()
    return True

def delete_transaction(transaction_id):
    """Deletes an existing transaction by its ID."""
    session = Session()
    transaction = session.query(Transaction).filter_by(id=transaction_id).first()
    
    if not transaction:
        session.close()
        return False
    
    session.delete(transaction)
    session.commit()
    session.close()
    return True