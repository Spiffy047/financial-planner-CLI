# lib/models.py

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

# ORM Base
Base = declarative_base()

class User(Base):
    """Represents a user of the finance tracker."""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    
    def __repr__(self):
        return f"<User(username='{self.username}')>"

class Category(Base):
    """Represents a financial transaction category."""
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    
    transactions = relationship("Transaction", back_populates="category")
    
    def __repr__(self):
        return f"<Category(name='{self.name}')>"

class Transaction(Base):
    """Represents a single financial transaction."""
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)  # 'income' or 'expense'
    date = Column(DateTime, default=datetime.now)
    description = Column(String)
    
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="transactions")
    
    def __repr__(self):
        return f"<Transaction(amount='{self.amount}', type='{self.type}', category='{self.category.name}')>"

class Budget(Base):
    """Represents a budget for a specific category and month."""
    __tablename__ = 'budgets'
    
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'), unique=True)
    limit = Column(Float, nullable=False)
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    
    category = relationship("Category")
    
    def __repr__(self):
        return f"<Budget(category='{self.category.name}', limit='{self.limit}', month='{self.month}', year='{self.year}')>"