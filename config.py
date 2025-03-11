from dotenv import load_dotenv
import os

load_dotenv()  

MONDAY_API_KEY = os.getenv("SECRET_KEY")

NULL_QUERY: {"query": ""}

get_columns_ids_names_by_id = {"query": "query { boards(ids: #BOARD) { items_page { items { name column_values { id } } } } }" }


