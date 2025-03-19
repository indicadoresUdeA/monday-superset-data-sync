import requests
import config 

MONDAY_API_URL = "https://api.monday.com/v2"
HEADERS = {
  "Authorization": config.MONDAY_API_KEY,
  "Content-Type": "application/json"
}

def get_board_items(board_id):
    query = 0 #Aqui viene el query for column
    response = requests.post(MONDAY_API_URL, json=query, headers=HEADERS)
    data = response.json()
    return data