import requests
import pandas as pd

# Function to fetch users in a specific league
def fetch_users_in_league(league_id):
    """
    The function `fetch_users_in_league` fetches users data from an API endpoint based on a league ID,
    converts it to a DataFrame, and saves it as a CSV file.
    
    :param league_id: The function `fetch_users_in_league(league_id)` is designed to fetch users in a
    specific league using the Sleeper API. It sends a GET request to the API endpoint for the specified
    league ID, retrieves the user data, converts it to a DataFrame using pandas, and then saves the data
    """
    # API endpoint for fetching users in a league
    url = f"https://api.sleeper.app/v1/league/{league_id}/users"
    
    # Making the API call
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        users_data = response.json()
        
        # Convert the JSON data to a DataFrame
        users_df = pd.DataFrame(users_data)
        
        # Specify the path where you want to save the CSV file
        csv_file_path = 'users_in_league.csv'
        
        # Save the DataFrame to a CSV file
        users_df.to_csv(csv_file_path, index=False)
        
        print(f"Users data saved to {csv_file_path}")
    else:
        print("Failed to fetch data. Please check the league ID and try again.")

# Example league ID (Replace this with your league's ID)
league_id_example = ""

# Fetching and saving the users data to a CSV file
fetch_users_in_league(league_id_example)
