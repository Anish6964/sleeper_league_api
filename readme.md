# Sleeper League Data Fetcher

This set of Python scripts interfaces with the Sleeper API to fetch and export data about users, players, and transactions within sleeper league. The data is exported in CSV format for easy import into Google Sheets or other data analysis tools.

## Dependencies

To install the required dependencies, run the following command in the terminal:

```pip install -r requirements.txt```

## Scripts

There are three main scripts in this project:

1. **fetch_users.py**: Fetches all users in a specified league.
2. **fetch_players.py**: Fetches all NFL players.
3. **fetch_transactions.py**: Fetches transactions for any given week(s) within a league.
