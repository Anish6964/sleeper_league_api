import requests
import pandas as pd

def fetch_transactions(league_id, week):
    """
    The function `fetch_transactions` fetches transaction data for a specific week from a given league
    using an API and saves it to a CSV file.
    
    :param league_id: League ID is the unique identifier for a specific fantasy football league. It is
    used to specify which league's transactions you want to fetch
    :param week: The `week` parameter in the `fetch_transactions` function represents the specific week
    for which you want to fetch transactions in a sleeper league. This parameter is used to
    specify the week for which you want to retrieve the transactions data from the Sleeper API
    """
    # API endpoint for fetching transactions for a given week
    url = f"https://api.sleeper.app/v1/league/{league_id}/transactions/{week}"
    
    # Making the API call
    response = requests.get(url)
    
    if response.status_code == 200:
        transactions = response.json()
        
        # Check if transactions were found
        if transactions:
            # Convert the list of transactions to a DataFrame
            transactions_df = pd.DataFrame(transactions)
            
            # Specify the path where you want to save the CSV file
            csv_file_path = f"transactions_week_{week}.csv"
            
            # Save the DataFrame to a CSV file
            transactions_df.to_csv(csv_file_path, index=False)
            
            print(f"Transactions for week {week} saved to {csv_file_path}")
        else:
            print(f"No transactions found for week {week}.")
    else:
        print(f"Failed to fetch transactions for week {week}. Status code: {response.status_code}")

# Inputs for the function
league_id = ""
week = 1  # The week for which you want to fetch transactions

# Fetching and saving the transactions to a CSV file
fetch_transactions(league_id, week)
