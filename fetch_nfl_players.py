import requests
import pandas as pd

# Function to fetch all NFL players
def fetch_nfl_players():
    """
    The function fetches NFL players data from an API, converts it to a DataFrame, and saves it to a CSV
    file.
    """
    # API endpoint for fetching all players, filtering by sport = "nfl"
    url = "https://api.sleeper.app/v1/players/nfl"
    
    # Making the API call
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        players_data = response.json()
        
        # Convert the JSON data to a list of dictionaries (one for each player)
        players_list = [value for key, value in players_data.items()]
        
        # Convert the list of dictionaries to a DataFrame
        players_df = pd.DataFrame(players_list)
        
        # Specify the path where you want to save the CSV file
        csv_file_path = 'nfl_players.csv'
        
        # Save the DataFrame to a CSV file
        players_df.to_csv(csv_file_path, index=False)
        
        print(f"NFL players data saved to {csv_file_path}")
    else:
        print("Failed to fetch NFL players data. Please try again later.")

# Fetching and saving the NFL players data to a CSV file
fetch_nfl_players()
