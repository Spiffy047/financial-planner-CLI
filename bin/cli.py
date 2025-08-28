import click
from lib.core import add_transaction, get_monthly_summary, get_transactions_as_list, update_transaction, delete_transaction
from lib.models import Base
from lib.database import Session, engine

@click.group()
def cli():
    """A CLI for tracking personal finances."""
    pass

@cli.command()
@click.option('--amount', type=float, required=True, help='Amount of the transaction.')
@click.option('--type', type=click.Choice(['expense', 'income']), required=True, help='Type of transaction.')
@click.option('--category', required=True, help='Category of the transaction.')
@click.option('--desc', default="", help='Description of the transaction.')
def add(amount, type, category, desc):
    """Adds a new transaction."""
    if amount <= 0:
        click.echo("Error: Amount must be a positive number.")
        return
    
    add_transaction(amount, type, category, desc)
    click.echo(f"Transaction added: {type.upper()} of ${amount:.2f} for '{category}'")

@cli.command()
def view_recent():
    """Views the 10 most recent transactions."""
    transactions = get_transactions_as_list(limit=10)
    if not transactions:
        click.echo("No transactions found. Add some with the 'add' command!")
        return
    
    click.echo("\n--- Recent Transactions ---")
    
    for t in transactions:
        click.echo(f"[{t['id']}] {t['date']}: {t['type'].upper(): <7} ${t['amount']:>8.2f} ({t['category']}) - {t['description']}")

@cli.command()
@click.option('--month', type=int, help="Month to summarize (1-12).", required=True)
@click.option('--year', type=int, help="Year to summarize.", required=True)
def summary(month, year):
    """Calculates a financial summary for a given month."""
    if not 1 <= month <= 12:
        click.echo("Error: Month must be between 1 and 12.")
        return
        
    income, expenses, balance = get_monthly_summary(month, year)
    
    click.echo(f"\n--- Financial Summary for {month}/{year} ---")
    click.echo(f"Total Income:   ${income:.2f}")
    click.echo(f"Total Expenses: ${expenses:.2f}")
    click.echo(f"Net Balance:    ${balance:.2f}")
    
@cli.command()
@click.argument('id', type=int, required=True)
@click.option('--amount', type=float, help='New amount for the transaction.')
@click.option('--type', type=click.Choice(['expense', 'income']), help='New type of transaction.')
@click.option('--category', help='New category of the transaction.')
@click.option('--desc', help='New description of the transaction.')
def update(id, amount, type, category, desc):
    """Updates an existing transaction by its ID.
    
    Specify the ID and one or more fields to update.
    """
    if not any([amount, type, category, desc]):
        click.echo("Error: At least one field (--amount, --type, --category, or --desc) must be provided to update.")
        return
    
    if update_transaction(id, amount, type, category, desc):
        click.echo(f"Transaction with ID {id} updated successfully.")
    else:
        click.echo(f"Error: Transaction with ID {id} not found.")

@cli.command()
@click.argument('id', type=int, required=True)
def delete(id):
    """Deletes a transaction by its ID."""
    if delete_transaction(id):
        click.echo(f"Transaction with ID {id} deleted successfully.")
    else:
        click.echo(f"Error: Transaction with ID {id} not found.")


if __name__ == '__main__':
    cli()
